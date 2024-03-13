
# Create your models here.
from django.db import models

class Telefonos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()

class Cargadores(models.Model):
    marca  = models.CharField(max_length=100)
    modelo = models.IntegerField()

class Accesorios(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.IntegerField()

# Create your models here.
