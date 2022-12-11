from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("5602141301:AAFIPIdCBI5MeJaxA9kq9OvDoleubUYvKws")
BOT_NAME = getenv("LogicalMusic) 
API_ID = int(getenv("API_ID", "10300036"))
API_HASH = getenv("79c295e05c970ddd724f0762ba275104")
BOT_USERNAME = getenv("LogicalMusicalbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5340784799").split()))
