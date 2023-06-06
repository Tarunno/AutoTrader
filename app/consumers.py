from channels.consumer import SyncConsumer, AsyncConsumer, StopConsumer
from time import sleep
import asyncio
from asgiref.sync import async_to_sync

class MySyncConsumer(SyncConsumer):
    
    def websocket_connect(self, event):
        print('Websocket Connected...', event)

        group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_add)(
            group_name, 
            self.channel_name
        )
        self.send({
            'type': 'websocket.accept'
        })
      
    def websocket_receive(self, event):
        print('Message Received...', event)
        group_name = self.scope['url_route']['kwargs']['group_name']
        async_to_sync(self.channel_layer.group_send)(group_name, {
            'type': 'bid.message',
            'msg': event['text']
        }) 

    def bid_message(self, event): # bid.message
        print('Event...', event)
        self.send({
            'type': 'websocket.send',
            'text': event['msg']
        })

    def websocket_disconnect(self, event):
        print('Websocket Disconnected', event)
        async_to_sync(self.channel_layer.group_discard)(
            'biders', self.channel_name
        )
        raise StopConsumer()


class MyAsyncConsumer(AsyncConsumer):
    
    async def websocket_connect(self, event):
        print('Websocket Connected...', event)
        group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_add(
            group_name, 
            self.channel_name
        )
        await self.send({
            'type': 'websocket.accept'
        })
      
    async def websocket_receive(self, event):
        print('Message Received...', event)
        group_name = self.scope['url_route']['kwargs']['group_name']
        await self.channel_layer.group_send(group_name, {
            'type': 'bid.message',
            'msg': event['text']
        })
      
    async def bid_message(self, event): # bid.message
        print('Event...', event)
        await self.send({
            'type': 'websocket.send',
            'text': event['msg']
        })

    async def websocket_disconnect(self, event):
        print('Websocket Disconnected', event)
        raise StopConsumer()

