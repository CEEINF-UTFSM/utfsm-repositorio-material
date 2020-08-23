from django.shortcuts import render
from django.http import JsonResponse


from ..models import Archivo


def archivo_list(request):
    archivos = Archivo.objects.all()
    return render(request, "archivos/aux_upload.html")
