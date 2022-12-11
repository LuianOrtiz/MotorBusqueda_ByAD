from django.db import models

# Create your models here.
class Indice(models.Model):
    url = models.URLField(max_length=300)
    analizado = models.BooleanField()
    palabra_1 = models.TextField(blank=True)
    palabra_2 = models.TextField(blank=True)
    palabra_3 = models.TextField(blank=True)
    
    def __str__(self):
        return self.url
