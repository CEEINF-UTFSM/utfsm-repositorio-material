from django.db import models
from django.contrib.auth.models import User

from ramos.models import Ramo
# Create your models here.
from django.core.validators import MinValueValidator, MaxValueValidator

class UserProfile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)


def path_of_file(instance, filename):
    return f"media/{instance.ramo.sigla}/{instance.tipo}/{filename}"


class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    ramo = models.ForeignKey(Ramo, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    aceptado = models.BooleanField(default=False)
    semestre = models.IntegerField(
        "semestre en que se genero el archivo", validators=[MinValueValidator(1), MaxValueValidator(11)])
    subido = models.DateTimeField(auto_now=False, auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    path = models.FileField(upload_to=path_of_file)
    def __str__(self):
        return self.nombre
