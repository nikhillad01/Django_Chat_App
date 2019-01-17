from channels.generic.websocket import AsyncWebsocketConsumer
import json

"""Consumer has set of events. and handles basic connection between client and server """

# AsyncWebsocketConsumer  has same methods like websocket consumer but everything is Async.

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):

        """This method used to create connection , scope has information like url ,
        room name etc and scopes are used for life long connection
        """
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name

        # Join room group
        await self.channel_layer.group_add(     # adds channel and room name to channel_layer group.
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        """This method is used to disconnect from group."""

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )



    async def receive(self, text_data):     # Receive message from WebSocket
        text_data_json = json.loads(text_data)  # message in json so parsing will be easy
        message = text_data_json['message']



        await self.channel_layer.group_send(    # Send message to room group
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )


    async def chat_message(self, event):      # Receive message from room group
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))