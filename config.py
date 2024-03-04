# importing all env variables
import os
from dotenv import load_dotenv

load_dotenv()

# load the environment variables
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_USENAME = os.getenv("TELEGRAM_BOT_USENAME")
TELEGRAM_BOT_NAME = os.getenv("TEMEGRAM_BOT_NAME")
TELEGRAM_PHONE_NUMBER = os.getenv("TELEGRAM_PHONE_NUMBER")