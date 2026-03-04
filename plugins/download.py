from pyrogram import filters, Client, Message  # ← YE ADD KARO
from client import app
from utils.helpers import is_url, fmtsize, resolve_cookies  # ← resolve_cookies bhi add
import yt_dlp
import os
import asyncio

@app.on_message(filters.text & filters.outgoing)  # Fixed filter
async def handle_url(client: Client, message: Message):  # Ab Client defined hai
    text = message.text
    if not is_url(text):
        return
    
    msg = await message.reply("📥 Downloading...")
    
    ydl_opts = {
        'outtmpl': f'/tmp/serenadl/%(title)s.%(ext)s',  # Fixed path
        'cookiefile': resolve_cookies(),  # YT Netscape cookies
        'format': 'best[height<=720]',
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(text, download=True)
            file_path = ydl.prepare_filename(info)
            
            ext = os.path.splitext(file_path)[1].lower()
            caption = f"**{info.get('title', 'Unknown')}**\n{fmtsize(info.get('filesize', 0))}"
            
            if ext in ['.mp4', '.mkv']:
                await msg.reply_video(file_path, caption=caption)
            elif ext == '.mp3':
                await msg.reply_audio(file_path, caption=caption)
            else:
                await msg.reply_document(file_path, caption=caption)
                
        os.remove(file_path)
        await msg.delete()
    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")
