# admin.py
from django.contrib import admin
from .models import MediaItem

# Registre o modelo MediaItem para aparecer no Django Admin
@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'latitude', 'longitude', 'local_image', 'film_image', 'other_image')  # Exibe as colunas na listagem
    search_fields = ('title', 'media_type')  # Adiciona uma barra de pesquisa
    list_filter = ('media_type',)  # Filtro para media_type
