from config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER
import configparser
import json
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events, sync
from telethon.tl.functions.messages import (GetHistoryRequest)
from telethon.tl.types import (PeerChannel)

# Replace these values with your own
api_id = TELEGRAM_API_ID
api_hash = TELEGRAM_API_HASH

# Here you define the target channel that you want to listen to:
user_input_channel = 'https://t.me/+8auXr4xpMnxhMWZl'
channel_id = -1001615795252 


# listener
async def main():
    # Create the client and connect
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start()
    print("Client Created")
    # Ensure you're authorized
    if not await client.is_user_authorized():
        await client.send_code_request(TELEGRAM_PHONE_NUMBER)
        try:
            await client.sign_in(TELEGRAM_PHONE_NUMBER, input('Enter the code: '))
        except SessionPasswordNeededError:
            await client.sign_in(password=input('Password: '))

    # Getting information about yourself
    me = await client.get_me()
    print(me.stringify())

    # Getting all the channels that I can access
    async for dialog in client.iter_dialogs():
        # print(dialog.name, 'has ID', dialog.id)
        pass

    # This is the channel ID for the channel I want to get messages from
    # channel = -1001615795252
    channel = user_input_channel
    # Convert it to a PeerChannel
    entity = await client.get_entity(channel)
    # How many messages to retrieve
    limit = 1
    # The offset ID for which we retrieve the messages
    offset_id = 0
    # The maximum ID for which we retrieve the messages
    max_id = 0
    # Get the history of the channel
    messages = await client(GetHistoryRequest(
        peer=entity,
        limit=limit,
        offset_date=None,
        offset_id=offset_id,
        max_id=max_id,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    # Iterate through all the messages while printing them
    for message in messages.messages:
        # print(message.message)
        # print("Message ID: ", message.id)
        pass

    # Add an event handler for new messages
    @client.on(events.NewMessage(chats=channel))
    async def handler(event):
        # When a new message is received print it
        # print(event.message.stringify())
        print(event.raw_text)

    print('Listening')
    # Run the client until Ctrl+C is pressed
    await client.run_until_disconnected()

with TelegramClient('anon', api_id, api_hash) as client:
    client.loop.run_until_complete(main())
    




