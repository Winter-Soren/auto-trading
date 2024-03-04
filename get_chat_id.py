from telethon.sync import TelegramClient
from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER

# Replace these values with your own
api_id = TELEGRAM_API_ID
api_hash = TELEGRAM_API_HASH
phone_number = TELEGRAM_PHONE_NUMBER

# Initialize a TelegramClient instance
client = TelegramClient('session_name', api_id, api_hash)

# Connect to the Telegram servers
client.start(phone=phone_number)

async def get_chat_id(chat_entity):
    try:
        # Get full information about the chat
        chat = await client.get_entity(chat_entity)
        print(f"Chat title: {chat.title}, ID: {chat.id}")
    except Exception as e:
        print(f"Error: {e}")

# Replace 'invite link or username' with the invite link or username of the group or channel
invite_link_or_username = 'https://t.me/+8auXr4xpMnxhMWZl'  # Example invite link

# Run the function to get the chat ID
client.loop.run_until_complete(get_chat_id(invite_link_or_username))

# Disconnect from the Telegram servers
client.disconnect()
