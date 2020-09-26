from django.contrib import admin

from .models import Archivo
from ramos.models import Ramo
# Register your models here.
admin.site.register(Archivo)
admin.site.register(Ramo)
