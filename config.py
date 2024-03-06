# importing all env variables
import os
from dotenv import load_dotenv

# load the environment variables
load_dotenv()

# telegram variables
TELEGRAM_API_ID = os.getenv("TELEGRAM_API_ID")
TELEGRAM_API_HASH = os.getenv("TELEGRAM_API_HASH")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
TELEGRAM_BOT_USENAME = os.getenv("TELEGRAM_BOT_USENAME")
TELEGRAM_BOT_NAME = os.getenv("TEMEGRAM_BOT_NAME")
TELEGRAM_PHONE_NUMBER = os.getenv("TELEGRAM_PHONE_NUMBER")


# firebase variables
FIREBASE_apiKey = os.getenv("FIREBASE_apiKey")
FIREBASE_authDomain = os.getenv("FIREBASE_authDomain")
FIREBASE_databaseURL = os.getenv("FIREBASE_databaseURL")
FIREBASE_projectId = os.getenv("FIREBASE_projectId")
FIREBASE_storageBucket = os.getenv("FIREBASE_storageBucket")
FIREBASE_messagingSenderId = os.getenv("FIREBASE_messagingSenderId")
FIREBASE_appId = os.getenv("FIREBASE_appId")
FIREBASE_measurementId = os.getenv("FIREBASE_measurementId")

# upstox variables
UPSTOX_API_KEY = os.getenv("UPSTOX_API_KEY")
UPSTOX_API_SECRET = os.getenv("UPSTOX_API_SECRET")
UPSTOX_REDIRECT_URI = os.getenv("UPSTOX_REDIRECT_URI")
UPSTOX_MOBILE_NUMBER = os.getenv("UPSTOX_MOBILE_NUMBER")
UPSTOX_PIN = os.getenv("UPSTOX_PIN")
UPSTOX_AUTH_URL = os.getenv("UPSTOX_AUTH_URL")

