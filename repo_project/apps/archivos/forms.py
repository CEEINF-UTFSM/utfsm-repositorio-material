from django import forms
from .models import Archivo


class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ("nombre", "ramo", "tipo", "semestre", "path")
