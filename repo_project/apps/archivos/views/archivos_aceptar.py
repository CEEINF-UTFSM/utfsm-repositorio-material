from ..models import Archivo


def archivos_aceptar(modeladmin, request, queryset):
    queryset.update(aceptado=True)


def archivos_rechazar(modeladmin, request, queryset):
    queryset.delete()
