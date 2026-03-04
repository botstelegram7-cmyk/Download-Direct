from pyrogram import filters
from pyrogram.types import Message
from client import app
from utils.helpers import is_url, fmtsize
import yt_dlp
import os

@app.on_message(filters.outgoing & filters.text & ~filters.private)  # filters.outgoing critical
async def handle_url(client: Client, message: Message):
    text = message.text
    if not is_url(text):
        return
    
    msg = await message.reply("📥 Downloading...")
    
    ydl_opts = {
        'outtmpl': f'{DLDIR}/%(title)s.%(ext)s',
        'cookiefile': resolve_cookies(),  # Netscape YT cookies
        'format': 'best[height<=720]',  # Telegram friendly
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(text, download=True)
            file_path = ydl.prepare_filename(info)
            
            # Send as video/audio/document based on ext
            ext = os.path.splitext(file_path)[1].lower()
            caption = f"**{info.get('title', 'Unknown')}**\n{fmtsize(info.get('filesize', 0))}"
            
            if ext in ['.mp4', '.mkv', '.avi']:
                await msg.reply_video(file_path, caption=caption)
            elif ext in ['.mp3', '.m4a']:
                await msg.reply_audio(file_path, caption=caption)
            else:
                await msg.reply_document(file_path, caption=caption)
                
        os.remove(file_path)  # Cleanup
        await msg.delete()
    except Exception as e:
        await msg.edit(f"❌ Error: {str(e)}")
      
