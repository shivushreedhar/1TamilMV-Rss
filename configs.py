# Coded by @SMDxTG - if Any Query Ask him Directly 

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file

# Telegram
API_ID = int(os.getenv("API_ID", "16073849"))
API_HASH = os.getenv("API_HASH", "e84dd69cd0504b8b45b2fd6a4e19068d")
USER_SESSION = os.getenv("USER_SESSION", "BQD1RHkAWE0_hYeF0aYArWXqouTiPJZ9CQnZSIoQzeM2rxRzbubMFNHWttI5BXhZOKi6KpbpxihRuNWQXYNzH97YangznwgiVZy9w5aEt0jks5KS61a4vRKdw4lD4efqCrT-IA3MU6UR_3XuqFxaKaNcCHdWdMfuAnkqHSDmMx2cNEqRTnU1_2b9CpioOr4_6EDfJPopmxSbH8AuyR1-XqnAKvNJnKpS6XDiBpQAetoJ82gmBCWrBF7j2puPd09JekAnhtMLp9uEiTgdlW3hdlfenBKI5066SdQ_-20c9807-NXcYL0OuZWvNbmv_Y4cm4CYE0Qs-rBX-Ep2EAbziS6GsRN4dgAAAAFJ-SbtAA") # Use Pyrogram V2 String Session 
#if you don't have string Gen bot - use it my bot @SMD_StringBot

# Web
PORT = int(os.getenv("PORT", "8080")) 
URL = os.getenv("URL", "https://tmv-rss-213001577ae6.herokuapp.com/") # Heroku or Koyeb Or Render Base Url 

# MongoDB
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://bsadmin:bsadmin12@cluster0.anisucu.mongodb.net/?appName=Cluster0") #Mongodb Url 
DATABASE_NAME = os.getenv("DATABASE_NAME", "Cluster0") # example Cluster0

# TamilMV settings
TMV_URL = os.getenv("TMV_URL", "https://www.1tamilmv.land/")
TMV_TORRENT = int(os.getenv("TMV_TORRENT", "-1003502593324"))
TMV_LEECH_GRP = int(os.getenv("TMV_LEECH_GRP", "-1003679562362"))
TMV_MIRROR_GRP = int(os.getenv("TMV_MIRROR_GRP", ""))
TMV_TORRENT_THUMB = os.getenv("TMV_TORRENT_THUMB", "https://graph.org/file/36f6cd17e608fdaa60074-a46133c3f65a9bc8ec.jpg") #torrant Pic
BOT_TAG = os.getenv("BOT_TAG", "@BSHEGDE5") # File Prefix

# Internal
PING_INTERVAL = int(os.getenv("PING_INTERVAL", "120"))
SCRAPE_INTERVAL = int(os.getenv("SCRAPE_INTERVAL", "300"))  # 5 min
SIZE_LIMIT_GB = int(os.getenv("SIZE_LIMIT_GB", 50))  # Default: 50 GB
