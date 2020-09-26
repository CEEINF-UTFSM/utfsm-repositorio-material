from django.contrib import admin

from .models import Archivo
from .views.archivos_aceptar import archivos_aceptar, archivos_rechazar
# Register your models here.


class ArchivoAdmin(admin.ModelAdmin):
    actions = [archivos_aceptar, archivos_rechazar]


admin.site.register(Archivo, ArchivoAdmin)
