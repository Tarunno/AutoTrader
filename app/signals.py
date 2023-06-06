from django.db.models.signals import post_save
from django.dispatch import receiver
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from .models import *
import json

@receiver(post_save, sender=Car)
def handle_database_update(sender, instance, group_name='biders', **kwargs):
    # Broadcast the update using Channels
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(group_name, {
        'type': 'bid.message',
        'msg': json.dumps({'msg':{
            'bid_value': str(instance.bid),
            'bid_id': str(instance.id)
        }})
    })
