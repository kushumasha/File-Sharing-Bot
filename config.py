#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8281450789:AAEMNniEQGyG3CemtO64PIdo3xiPEIjIuBo")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "14689508"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "79413cfe2d8cc93ddf1815ef588e80d5")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002819669622"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7484783061"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://s3614371925809272310:s3614371925809272310@cluster0.ufhhuzj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002792211269"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLED", None)

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "0"))

#start message
START_PIC = os.environ.get("START_PIC","https://graph.org/file/3e4eb3a61c207944b19fb-d9a894afb5e44ef953.jpg")
START_MSG = os.environ.get("START_MESSAGE", "╭──────────────────⦿
│ ▸ ʜᴇʏ {first}\n\n<b>🤗
│ ▸ Tʜɪs Is  ˹ Fɪʟᴇ Sʜᴀʀᴇ Bᴏᴛ ˼ 
├───────────────────⦿
│ ▸ ᴛʜɪs ɢʀᴏᴜᴘ ʜᴀᴠᴇ sᴘᴇᴄɪᴀʟ ᴘᴏᴡᴇʀ .
│ ▸ᴛʜɪs ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ.
├───────────────────⦿
│ ▸ ʙᴏᴛ ғᴏʀ ᴛᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘs.
│ ▸ ʙᴏᴛ ғᴏʀ ғɪʟᴇ sᴛᴏʀᴇ .
│ ▸ ʏᴏᴜ ᴄᴀɴ sᴛᴏʀᴇ ʏᴏᴜʀ ʙɪɢ ғɪʟᴇ .
│ ▸ 📂 ғɪʟᴇ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴᴅ sʜᴀʀᴇ ᴛᴏ 
│ ʏᴏᴜʀ ғʀɪᴇɴᴅ ʟɪᴋᴇ ᴡᴏᴡ
│ ▸ 24x7 ᴏɴʟɪɴᴇ sᴜᴘᴘᴏʀᴛ
├───────────────────⦿
│ ᴡᴇ ᴡɪʟʟ ᴀᴅᴅ ᴍᴏʀᴇ ➕ ᴛʜɪɴɢs 
│ ᴍᴀᴅᴇ ʙʏ... @Nobita_X_Surya 
╰───────────────────⦿ 
➻ ᴀ ғᴀsᴛ & ᴘᴏᴡᴇʀғᴜʟ ᴛᴇʟᴇɢʀᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ.
──────────────────")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7484783061 7169497576").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hi {first}\n\n<b>✨

Tʜɪs Is Tʜᴇ Bɪɢɢᴇsᴛ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ 📂

┌────── ˹ ᴡʜʏ ʏᴏᴜ ᴊᴏɪɴ ˼───⏤‌‌●
┆◍ ʜєʏ, {first}\n\n<b>🥀
┆◍ ɪ ᴧϻ ˹File Store Bot ˼
└──────────────────────• 

ɪ ᴀᴍ ᴛʜᴇ ғᴀsᴛᴇsᴛ ᴀɴᴅ ᴘᴏᴡᴇʀғᴜʟʟ Fɪʟᴇ Sᴛᴏʀᴇ Bᴏᴛ 
➥ Mᴀᴋᴇ Yᴏᴜʀ Fɪʟᴇ ʟɪɴᴋ 🔗
➥ Fᴏʀ Jᴏɪɴ Yᴏᴜ A Wɪʟʟ A ❣ Pʀᴇᴍɪᴜᴍ Mᴇᴍʙᴇʀ .
•──────────────────────•
✦ᴘᴏᴡєʀєᴅ ʙʏ » Sᴜʀʏᴀ 🜲
•──────────────────────•")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
