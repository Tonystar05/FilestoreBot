import os
from os import environ
import logging
from logging.handlers import RotatingFileHandler



BOT_TOKEN = os.environ.get("BOT_TOKEN", "6722606812:AAEdb3pmMLJhK_qHhJsA5eT03bKtgl2SrjQ")
API_ID = int(os.environ.get("API_ID", "15529802"))
API_HASH = os.environ.get("API_HASH", "92bcb6aa798a6f1feadbc917fccb54d3")


# add premium logs channel id
PAYMENT_LOGS = int(environ.get('PAYMENT_LOGS', '-1001868871195'))

#Shortner (token system) 
"""
some token verification sites
https://dashboard.shareus.io/
"""

# Turn this feature on or off using True or False put value inside  ""
# TRUE for yes FALSE if no 
USE_SHORTLINK = True if os.environ.get('USE_SHORTLINK', "FALSE") == "TRUE" else False 
# only shareus service known rightnow rest you can test on your own
SHORTLINK_API_URL = os.environ.get("SHORTLINK_API_URL", "api.shareus.io")
# SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "")
#use this key if not working ☠️ (jokin!!)
SHORTLINK_API_KEY = os.environ.get("SHORTLINK_API_KEY", "")
#add your custom time in secs for shortlink expiration.
# 24hr = 86400
# 12hr = 43200
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', "86400")) # Add time in seconds
#Tutorial video for the user of your shortner on how to download.
TUT_VID = os.environ.get("TUT_VID","https://t.me/How_to_Download_7x/32")


#Payment to remove the token system
#put TRUE if you want this feature
USE_PAYMENT = True if (os.environ.get("USE_PAYMENT", "FALSE") == "TRUE") & (USE_SHORTLINK) else False
#UPI ID
UPI_ID = os.environ.get("UPI_ID", " ")
#UPI QR CODE IMAGE
UPI_IMAGE_URL = os.environ.get("UPI_IMAGE_URL", "")
#SCREENSHOT URL of ADMIN for verification of payments
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", "")
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "30 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "110 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "299 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "550 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "999 rs")


OWNER_ID = int(os.environ.get("OWNER_ID", "821215952"))
DB_URL = os.environ.get("DB_URL", "mongodb+srv://2gbRenameAUG:2gbRenameAUG@cluster0.uaysx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DB_NAME", "FileStoreXeon2Bot")


CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002203107302"))
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001942242411"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001690762284"))
FORCE_SUB_CHANNEL3 = int(os.environ.get("FORCE_SUB_CHANNEL3", "-1001804728701"))

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "600")) # auto delete in seconds


PORT = os.environ.get("PORT", "8080")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))



try:
    ADMINS=[7085541484]
    for x in (os.environ.get("ADMINS", "5829753916 821215952").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")









CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

DISABLE_CHANNEL_BUTTON = True if os.environ.get('DISABLE_CHANNEL_BUTTON', "True") == "True" else False

BOT_STATS_TEXT = "<b>BOT UPTIME :</b>\n{uptime}"







USER_REPLY_TEXT = "❌Don't Send Me Messages Directly I'm Only File Share Bot !"

START_MSG = os.environ.get("START_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ")
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "ʜᴇʟʟᴏ {mention}\n\n<b>ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ ʙᴜᴛᴛᴏɴ ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.</b>")


START_PIC = os.environ.get("START_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://telegra.ph/file/e292b12890b8b4b9dcbd1.jpg")






ADMINS.append(OWNER_ID)
ADMINS.append(7085541484)

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
   





# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @Madflix_Bots
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
