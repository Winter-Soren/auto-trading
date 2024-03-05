from typing import Union
from telethon import TelegramClient, events
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import GetHistoryRequest

class TelegramMessageListener:
    global_event = None
    
    def __init__(self, api_id: str, api_hash: str, user_input_channel: Union[int, str], phone_number: str):
        self.api_id = api_id
        self.api_hash = api_hash
        self.user_input_channel = user_input_channel
        self.phone_number = phone_number

    async def start(self):
        await self._main()


    async def _main(self) -> None:
        # Create the client and connect
        self.client = TelegramClient(f'session_{self.api_id}', self.api_id, self.api_hash)
        await self.client.start()
        print("Client Created")
        
        # Ensure you're authorized
        if not await self.client.is_user_authorized():
            await self.client.send_code_request(self.phone_number)
            try:
                await self.client.sign_in(self.phone_number, input('Enter the code: '))
            except SessionPasswordNeededError:
                await self.client.sign_in(password=input('Password: '))

        # Getting information about yourself
        me = await self.client.get_me()
        print(me.stringify())   

        # Retrieve messages
        channel = self.user_input_channel
        entity = await self.client.get_entity(channel)
        limit = 1 
        offset_id = 0 
        max_id = 0 
        messages = await self.client(GetHistoryRequest(
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
        @self.client.on(events.NewMessage(chats=channel))
        async def handler(event):
            self.global_event = event
            print("event from global event: ", self.global_event.raw_text)

        print("Listening for new messages...")

        await self.client.run_until_disconnected()
        
        print("Client Disconnected")