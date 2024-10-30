from django.db import models

# Create your models here.
class MediaItem(models.Model):
    title = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    media_type = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media', default='media/media_images/film.png')

    def __str__(self):
        return self.title