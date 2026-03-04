from pyrogram import filters, Client, Message  # ← YE ADD KARO
from client import app

@app.on_message(filters.command("start") & filters.outgoing)
async def start_cmd(client: Client, message: Message):
    await message.reply("🚀 **SerenaBot Started!**\nUniversal Downloader - Send URL!")

@app.on_message(filters.command("ping") & filters.outgoing)
async def ping(client: Client, message: Message):
    await message.reply("🏓 Pong!")
