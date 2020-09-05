from django.shortcuts import render
from ..serializers import ArchivoSerializer
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Archivo
from ramos.models import Ramo

@api_view(["GET"])
def archivo_list(request):
    archivos = Archivo.objects.all()
    serializer = ArchivoSerializer(archivos, many=True)
    return JsonResponse(serializer.data, safe=False)
    