import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = 'LeoMediaSearchBot'
USER_SESSION = 'User_Bot'
API_ID = 13413587
API_HASH = 'fa2829fb6fb89a42f0d3ad78bd4d8cb8'
BOT_TOKEN = '6493798968:AAFlmOG0I6S9-4zoJZaIOdMpvVF7eS79Ksw'

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = ['1085998540']
CHANNELS = [-1002038797131]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = -1001398786468
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = "mongodb+srv://wixoh61093:E7LSrvkiaq3X1uCu@cluster0.yjizf0a.mongodb.net/?retryWrites=true&w=majority"
DATABASE_NAME = 'cinee'
COLLECTION_NAME = 'channel_files'

# Messages
default_start_msg = """
**Hi, I'm Media Search Bot or ypu can call me as Auto-Filter Bot**
Here you can search files in Inline mode as well as PM, Use the below buttons to search files or send me the name of file to search.
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "")
OMDB_API_KEY = "cca8a5e"
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
