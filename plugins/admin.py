from pyrogram import filters, Client
from pyrogram.types import Message
from client import app
from config import OWNERIDS

@app.on_message(filters.command("stats") & filters.outgoing)
async def stats(client: Client, message: Message):
    if message.from_user.id not in OWNERIDS:
        return await message.reply("Owner only!")
    await message.reply("📊 Stats: Working fine!")
