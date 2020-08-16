from django.shortcuts import render
from ..serializers import ArchivoSerializer
from django.http import JsonResponse

from rest_framework.decorators import api_view


from ..models import Archivo


@api_view(["GET"])
def archivo_list(request):
    archivos = Archivo.objects.all()
    serializer = ArchivoSerializer(archivos, many=True)
    return JsonResponse(serializer.data, safe=False)
