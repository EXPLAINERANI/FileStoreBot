import os

API_ID = int(os.environ.get("API_ID",708575))
API_HASH = os.environ.get("API_HASH", 431d3ae02dd51dd7c26ab9f9a08dae84)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
DB_CHANNEL_ID = os.environ.get("-1002239324287")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("1685470205"))
UPDATE_CHANNEL = os.environ.get('-1002239324287', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(1685470205)
