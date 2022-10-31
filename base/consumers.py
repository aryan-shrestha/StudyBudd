import json
from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from base.models import Message, Room, User

class ChatConsumer(AsyncWebsocketConsumer): 
    async def connect(self):
        self.user = self.scope["user"]
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()
    
    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    # receive message from websocket
    async def receive(self, text_data):
        print("received()")
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        sender = {
            "id": self.user.id,
            "username": self.user.username,
            "avatar": self.user.avatar.url
        }
        
        message_obj = await self.save_message(message)

        # sending message to room group
        await self.channel_layer.group_send(
            self.room_group_name,{
                'type': 'chat_message',
                'message': message,
                'sender': sender
            }
        )

    # Receive message from room group
    
    async def chat_message(self, event):
        message = event['message']
        sender = event['sender']

        # send message to webSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'sender': sender
        }))

    @database_sync_to_async
    def save_message(self, message):
        room = Room.objects.get(slug=self.room_name)
        room.participants.add(self.user)
        message = Message.objects.create(user=self.user, room=room, body=message)
        return message