import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_group_name = 'chat_global'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

        # Enviar mensaje de bienvenida al servidor
        await self.send(text_data=json.dumps({
            'message': 'Bienvenido al Chat',
            'user': 'Servidor',
        }))

        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        print(f"{self.channel_name} left the group {self.room_group_name}")

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        user = self.scope["user"].username
        print(f"Message received: {message} from {user}")

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'user': user,
            }
        )

    async def chat_message(self, event):
        message = event['message']
        user = event['user']

        print(f"Broadcasting message: {message} from {user}")

        await self.send(text_data=json.dumps({
            'message': message,
            'user': user,
        }))

