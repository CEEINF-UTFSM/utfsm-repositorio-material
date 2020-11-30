from django.db import models

# Create your models here.


class Ramo(models.Model):
    sigla = models.CharField(max_length=50)
    nombre = models.CharField(max_length=255)
    semestre = models.IntegerField("semestre en que se cursa el ramo")
    def __str__(self):
        return f"{self.sigla}"


class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    ramos = models.ManyToManyField(Ramo)
    