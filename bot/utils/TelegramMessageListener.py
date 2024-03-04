from typing import Union
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest

class TelegramMessageListener:
    
    def __init__(self, api_id: str, api_hash: str, user_input_channel: Union[int, str], phone_number: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.user_input_channel = user_input_channel
        self.phone_number = phone_number
        self._main()

    async def _main(self) -> None:
        # Create the client and connect
        client = TelegramClient(f'session_{self.api_id}', self.api_id, self.api_hash)
        await client.start()
        print("Client Created")
        
        # Ensure you're authorized
        if not await client.is_user_authorized():
            await client.send_code_request(self.phone_number)
            try:
                await client.sign_in(self.phone_number, input('Enter the code: '))
            except SessionPasswordNeededError:
                await client.sign_in(password=input('Password: '))

        # Getting information about yourself
        me = await client.get_me()
        print(me.stringify())

        # Retrieve messages
        channel = self.user_input_channel
        entity = await client.get_entity(channel)
        limit = 1 
        offset_id = 0 
        max_id = 0 
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

        # Add an event handler for new messages
        @client.on(events.NewMessage(chats=channel))
        async def handler(event):
            print(event.raw_text)

        print("Listening for new messages...")

        await client.run_until_disconnected()

# Example usage:
if __name__ == "__main__":
    api_id = "your_api_id"
    api_hash = "your_api_hash"
    user_input_channel = "your_channel"
    phone_number = "your_phone_number"

    listener = TelegramMessageListener(api_id, api_hash, user_input_channel, phone_number)
