# serializers.py
from rest_framework import serializers
from .models import MediaItem

class MediaItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaItem
        fields = ['id', 'title', 'latitude', 'longitude', 'media_type', 'image']
        