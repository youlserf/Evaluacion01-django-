from django.db import models

# Create your models here.
class Region(models.Model):
    region_nombre = models.CharField(max_length=50)

class Candidato(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    nombres = models.CharField(max_length=200)
    apellidos = models.CharField(max_length=200)
    partido_politico = models.CharField(max_length=200)

    
