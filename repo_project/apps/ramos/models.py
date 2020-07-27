from django.db import models

# Create your models here.


class Ramo(models.Model):
    sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)


class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    ramos = models.ManyToManyField(Ramo)
