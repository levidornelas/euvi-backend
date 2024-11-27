from django.db import models

class MediaItem(models.Model):
    title = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    media_type = models.CharField(max_length=50)
    local_image = models.ImageField(upload_to='media', default='media/media_images/film.png')
    film_image = models.ImageField(upload_to='media', default='media/media_images/film.png')
    other_image = models.ImageField(upload_to='media', default='media/media_images/film.png', null=True, blank=True)
    general_info = models.TextField()  # Campo para informações gerais
    opening_hours = models.CharField(max_length=100, blank=True, null=True)  # Campo para o horário de funcionamento
    location = models.CharField(max_length=255)
    details = models.TextField()  

    def __str__(self):
        return self.title