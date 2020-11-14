from django.contrib import admin

from .models import Archivo
from ramos.models import Ramo
# Register your models here.


class ArchivosAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'aceptado']
    actions = ['archivos_aceptar']

    def archivos_aceptar(self, request, queryset):
        queryset.update(aceptado=True)
    archivos_aceptar.short_description = 'Aceptar archivo(s)'


admin.site.register(Archivo, ArchivosAdmin)
admin.site.register(Ramo)
