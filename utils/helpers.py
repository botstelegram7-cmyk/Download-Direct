import os
import re
import asyncio
from pathlib import Path

def resolve_cookies():
    """Auto-detect Netscape cookies from env and write to file"""
    yt_cookies = os.getenv("YTCOOKIES", "").strip()
    if yt_cookies and ('Netscape' in yt_cookies or '# Netscape HTTP Cookie File' in yt_cookies or '.youtube.com' in yt_cookies):
        cookie_file = Path("/tmp/cookies.yt.txt")
        cookie_file.write_text(yt_cookies)
        print(f"COOKIES: YTCOOKIES wrote {cookie_file} ({len(yt_cookies)} chars)")
        return str(cookie_file)
    return None

def is_url(text):
    url_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    return bool(url_pattern.search(text))

def fmtsize(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024
    return f"{size_bytes:.1f} TB"
