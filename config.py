import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "Music player")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
OWNER_NAME = getenv("OWNER_NAME", "deepakjack")
ALIVE_NAME = getenv("ALIVE_NAME", "Musicplayer")
BOT_USERNAME = getenv("BOT_USERNAME", "music")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "music")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "UnitedSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "shukurenai007")
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "http://telegra.ph/file/2a4e5b315fca98bec2c3f.png")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/shukurenai007/MusicPlayer")
IMG_1 = getenv("IMG_1", "https://telegra.ph/file/47519749bc82eaef2e0b6.png")
IMG_2 = getenv("IMG_2", "https://telegra.ph/file/d61b82c2f73ad9e98f849.png")
IMG_3 = getenv("IMG_3", "https://telegra.ph/file/5ad8ca83b4f52e9672c91.png")
IMG_4 = getenv("IMG_4", "https://telegra.ph/file/8abf152a3336f022c0c11.png")
