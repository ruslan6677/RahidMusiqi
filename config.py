from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("5751318375:AAFYAM2_5qq58z0Lm-nd0klQn_q35J49nTE")
BOT_NAME = getenv("BOT_NAME", "Chimney Music") 
API_ID = int(getenv("API_ID", "10300036"))
API_HASH = getenv("79c295e05c970ddd724f0762ba275104")
BOT_USERNAME = getenv("BOT_USERNAME", "CmineyMusicalbot")
PMPERMIT = getenv("PMPERMIT", "ENABLE")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5340784799").split()))
