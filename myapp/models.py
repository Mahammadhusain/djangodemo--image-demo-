from django.db import models

# Create your models here.

class HotelModel(models.Model):
    name = models.CharField(max_length=255)
    pic = models.ImageField(upload_to = 'Hotel')

    def __str__(self):
        return self.name