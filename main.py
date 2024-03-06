from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import PeerChannel

api_id = TELEGRAM_API_ID
api_hash = TELEGRAM_API_HASH
user_input_channel = "https://t.me/+8auXr4xpMnxhMWZl"
global_event = None


async def main():
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
    channel = user_input_channel

    @client.on(events.NewMessage(chats=channel)) 
    async def handler(event):
        global_event = event
        print(global_event.raw_text)

    print("Listening")
    await client.run_until_disconnected()


with TelegramClient("anon", api_id, api_hash) as client:
    client.loop.run_until_complete(main())
