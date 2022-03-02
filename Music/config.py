##Config

from os import getenv
from dotenv import load_dotenv

load_dotenv()
get_queue = {}
SESSION_NAME = getenv('SESSION_NAME', 'session')
BOT_TOKEN = getenv('BOT_TOKEN')
API_ID = int(getenv('API_ID', "9572580"))
API_HASH = getenv('API_HASH')
DURATION_LIMIT = int(getenv('DURATION_LIMIT', '30'))
COMMAND_PREFIXES = list(getenv('COMMAND_PREFIXES', '/ . , : ; !').split())
MONGO_DB_URI = getenv("MONGO_DB_URI")
SUDO_USERS = list(map(int, getenv('SUDO_USERS', '').split()))
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", '-1001457744346'))
ASS_ID = int(getenv("ASS_ID", '1825122580'))
OWNER_ID = list(map(int, getenv('OWNER_ID', '').split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", None)
