from channels.generic.websocket import AsyncWebsocketConsumer
import json

class YourConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data = json.loads(text_data)
        # Traitez les données reçues ici

        # Exemple d'envoi de données au client
        await self.send(text_data=json.dumps({
            'message': 'Hello, WebSocket!'
        }))