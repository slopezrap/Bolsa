
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from .tasks import MensajeAlGrupo

class Consumidor(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room group
        await self.channel_layer.group_add(
            'grupo',
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            'grupo',
            self.channel_name
         )
        
    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        if str(message) == "hola":
            MensajeAlGrupo.delay()
        else:
            
            # Send message to room group
            await self.channel_layer.group_send(
                'grupo',
                {
                    'type': 'chat_message',
                    'message': message
                }
            )
            
    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
    
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))