import os
import logging
import re
from telethon.errors import SessionPasswordNeededError
from telethon import TelegramClient, events
from config.config import TELEGRAM_API_ID, TELEGRAM_API_HASH, TELEGRAM_PHONE_NUMBER
from pipes import auth
from utils import parse_trade_message, get_closer_expiry_instrument, parse_new_trade_message
from api import place_order




api_id = TELEGRAM_API_ID
api_hash = TELEGRAM_API_HASH
user_input_channel = "https://t.me/+8auXr4xpMnxhMWZl"
global_event = None

async def Bot():
    client = TelegramClient("session_name", api_id, api_hash)
    await client.start()

    if not await client.is_user_authorized():
        await client.send_code_request(TELEGRAM_PHONE_NUMBER)
        try:
            await client.sign_in(TELEGRAM_PHONE_NUMBER, input("Enter the code: "))
        except SessionPasswordNeededError:
            await client.sign_in(password=input("Password: "))

    me = await client.get_me()
    print(f"Welcome: {me.first_name}, your ID is: {me.id}, and your username is: @{me.username}")

    try:
        print("Authenticating Upstox")
        # auth()
        print("Authenticated Upstox")
    except Exception as e:
        print(f"An error occurred in auth pipeline: {e}")

    channel = user_input_channel
    # @client.on(events.NewMessage(chats=channel)) 
    # async def handler(event):
    #     global global_event
    #     global_event = event
    #     print(f"Received new message: {global_event.raw_text}")

    @client.on(events.NewMessage(chats=channel, pattern=None))
    async def handler(event):
        global global_event
        global_event = event

        print(f"Received new message: {global_event.raw_text}")

        # Parse the message
        parsed_message = parse_new_trade_message(global_event.raw_text)
        print("Parsed message: ", parsed_message)
        
        # print("Parsed message: ", parsed_message)
        # dataset_path = "./data/response_Nifty 50.json"
        # target_index = parsed_message['index']
        # num_closer_expiry = 1
        # closer_expiry_instruments = get_closer_expiry_instrument(dataset_path, target_index, num_closer_expiry)        
        # print(closer_expiry_instruments[0]['instrument_key'])

        # Place the BUY order
        # params = {
        #     "quantity": 1,
        #     "product": "D",
        #     "validity": "DAY",
        #     "price": 0,
        #     "tag": "string",
        #     "instrument_token": closer_expiry_instruments[0]['instrument_key'],
        #     "order_type": "MARKET",
        #     "transaction_type": parsed_message['action'],
        #     "disclosed_quantity": 0,
        #     "trigger_price": 0,
        #     "is_amo": False
        # }

        # try:
        #     placed_order_response = place_order(params)

        #     # print("response ", placed_order_response)

        #     if placed_order_response:
        #         print(f"Order placed: {placed_order_response['data']}, for the params: {params}")
        #     else:
        #         print(f"Error placing order for the params: {params}")

        # except Exception as e:
        #     print("bhai order place nhi hora", e)



    print("Listening to the channel for messages...")
    await client.run_until_disconnected()

