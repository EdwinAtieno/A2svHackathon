<<<<<<< HEAD
# import json
# from channels.generic.websocket import AsyncWebsocketConsumer

# class ChatConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         if self.scope['user'].is_authenticated:
#             self.room_name = self.scope['user'].email[:5]
#             self.room_group_name = f'chat_{self.room_name}'

#             # Join user-specific room group
#             await self.channel_layer.group_add(
#                 self.room_group_name,
#                 self.channel_name
#             )

#             await self.accept()
#         else:
#             await self.close()

#     async def disconnect(self, close_code):
#         # Leave user-specific room group
#         await self.channel_layer.group_discard(
#             self.room_group_name,
#             self.channel_name
#         )

#     async def receive(self, text_data):
#         text_data_json = json.loads(text_data)
#         message = text_data_json['message']

#         if self.scope['user'].is_authenticated:
#             # Process financial advice request and send back the advice
#             advice = process_advice_request(self.scope['user'], message)

#             # Send advice to user-specific room group
#             await self.channel_layer.group_send(
#                 self.room_group_name,
#                 {
#                     'type': 'chat_message',
#                     'message': advice
#                 }
#             )

#     async def chat_message(self, event):
#         message = event['message']

#         await self.send(text_data=json.dumps({
#             'message': message
#         }))
=======
import json
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        if self.scope['user'].is_authenticated:
            self.room_name = self.scope['user'].email[:5]
            self.room_group_name = f'chat_{self.room_name}'

            # Join user-specific room group
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )

            await self.accept()
        else:
            await self.close()

    async def disconnect(self, close_code):
        # Leave user-specific room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        if self.scope['user'].is_authenticated:
            # Process financial advice request and send back the advice
            advice = process_advice_request(self.scope['user'], message)

            # Send advice to user-specific room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'chat_message',
                    'message': advice
                }
            )

    async def chat_message(self, event):
        message = event['message']

        await self.send(text_data=json.dumps({
            'message': message
        }))
>>>>>>> b8850a88e867fbc4218a3b049933cbd1d8d0118e
