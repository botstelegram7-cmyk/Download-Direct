from pyrogram import Client
import os

app = Client(
    "serena",
    api_id=os.getenv("APIID"),
    api_hash=os.getenv("APIHASH"),
    bot_token=os.getenv("BOTTOKEN"),
    in_memory=True,  # Critical for Render - no .session file
    workers=4
)
