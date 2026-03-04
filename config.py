import os

BOTTOKEN = os.getenv("BOTTOKEN")
APIID = int(os.getenv("APIID"))
APIHASH = os.getenv("APIHASH")
OWNERIDS = [int(x) for x in os.getenv("OWNERIDS", "1598576202").split(",")]
OWNERUSERNAME = os.getenv("OWNERUSERNAME", "XioquiXan")
SUPPORTUSERNAME = os.getenv("SUPPORTUSERNAME", "TechnicalSerena")
FREELIMIT = int(os.getenv("FREELIMIT", "3"))
BASICLIMIT = int(os.getenv("BASICLIMIT", "15"))
PREMIUMLIMIT = int(os.getenv("PREMIUMLIMIT", "50"))
DBPATH = os.getenv("DBPATH", "/tmp/serenadbbot.db")
DLDIR = os.getenv("DLDIR", "/tmp/serenadl")
PORT = int(os.getenv("PORT", "10000"))

