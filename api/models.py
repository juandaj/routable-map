from django.db import models

class Ubicacion(models.Model):
    name = models.CharField(max_length=20)
    latitud = models.CharField(max_length=20)
    longitud = models.CharField(max_length=20)

    class Meta:
        unique_together = ('latitud', 'longitud',)