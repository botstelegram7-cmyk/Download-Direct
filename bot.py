import os
import sys
import asyncio
from client import app
from config import *
import plugins.start
import plugins.download
import plugins.admin  # Import BEFORE app.start

async def main():
    os.makedirs(DLDIR, exist_ok=True)
    cookie_file = resolve_cookies()  # YT Netscape cookies load
    print("🚀 SerenaBot starting... Cookies:", cookie_file)
    
    await app.start()
    print("✅ Bot started successfully")
    
    # Flask for Render keep-alive
    from webapp import app as flask_app
    import threading
    threading.Thread(target=lambda: flask_app.run(host="0.0.0.0", port=PORT, debug=False), daemon=True).start()
    
    await asyncio.Event().wait()  # Keep running

if __name__ == "__main__":
    asyncio.run(main())
