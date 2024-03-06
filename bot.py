from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events
import logging
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER
from .pipes import auth


api_id = TELEGRAM_API_ID
api_hash = TELEGRAM_API_HASH
user_input_channel = "https://t.me/+8auXr4xpMnxhMWZl"
global_event = None


async def Bot():
    client = TelegramClient("session_name", api_id, api_hash)
    await client.start()
    print("Client Created")
    if not await client.is_user_authorized():
        await client.send_code_request(TELEGRAM_PHONE_NUMBER)
        try:
            await client.sign_in(TELEGRAM_PHONE_NUMBER, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Password: "))

    me = await client.get_me()
    print(f"Welcome: {me.first_name}, your ID is: {me.id}, and your username is: @{me.username}")

    print("Authenticating Upstox")
    auth()
    print("Authenticated Upstox")


    channel = user_input_channel
    @client.on(events.NewMessage(chats=channel)) 
    async def handler(event):
        global_event = event
        print(global_event.raw_text)

    print("Listening to the channel for messages...")
    await client.run_until_disconnected()