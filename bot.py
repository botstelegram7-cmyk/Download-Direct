import os
import sys
import asyncio
from client import app
from config import *  # Loads DLDIR etc.

# IMPORT ALL PLUGINS BEFORE app.start() - CRITICAL!
import plugins.start
import plugins.download  
import plugins.admin

# Create directories
os.makedirs(os.getenv("DLDIR", "/tmp/serenadl"), exist_ok=True)

async def main():
    from utils.helpers import resolve_cookies
    cookie_file = resolve_cookies()
    print("🚀 SerenaBot starting... Cookies:", cookie_file)
    
    await app.start()
    print("✅ Bot started successfully")
    
    # Flask keep-alive for Render
    from webapp import app as flask_app
    import threading
    threading.Thread(target=lambda: flask_app.run(host="0.0.0.0", port=int(os.getenv("PORT", 10000)), debug=False), daemon=True).start()
    
    await asyncio.Event().wait()

if __name__ == "__main__":
    asyncio.run(main())
