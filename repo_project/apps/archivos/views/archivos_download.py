from django.shortcuts import render
from django.http import JsonResponse

<<<<<<< HEAD
=======
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
>>>>>>> 625f8cf36533629d9ef0062ae7f147b017a48f21

from ..models import Archivo


def archivo_list(request):
    archivos = Archivo.objects.all()
    return render(request, "archivos/aux_upload.html")
