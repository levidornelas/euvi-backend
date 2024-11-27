# serializers.py
from rest_framework import serializers
from .models import MediaItem

class MediaItemSerializer(serializers.ModelSerializer):
    local_image = serializers.ImageField()
    film_image = serializers.ImageField()
    other_image = serializers.ImageField(allow_null=True, required=False)

    class Meta:
        model = MediaItem
        fields = ['id', 'title', 'latitude', 'longitude', 'media_type', 'local_image', 'film_image', 'other_image', 'general_info', 'opening_hours', 'location', 'details']
