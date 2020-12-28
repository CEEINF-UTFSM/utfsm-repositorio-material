from django.contrib import admin

from .models import Archivo
from ramos.models import Ramo
from ramos.models import Carrera


# Register your models here.
admin.site.register(Archivo)
admin.site.register(Ramo)
admin.site.register(Carrera)
