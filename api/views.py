from rest_framework import viewsets
from .models import MediaItem
from .serializers import MediaItemSerializer

class MediaItemViewSet(viewsets.ModelViewSet):
    queryset = MediaItem.objects.all()
    serializer_class = MediaItemSerializer