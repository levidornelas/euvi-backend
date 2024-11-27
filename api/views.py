from rest_framework import viewsets
from .models import MediaItem
from .serializers import MediaItemSerializer
from rest_framework.permissions import IsAuthenticated 

class MediaItemViewSet(viewsets.ModelViewSet):
    """
    ViewSet para listar, criar, atualizar e excluir MediaItem.
    """
    queryset = MediaItem.objects.all()  # Define a consulta para pegar todos os objetos
    serializer_class = MediaItemSerializer  # Usa o serializer para definir o formato dos dados

