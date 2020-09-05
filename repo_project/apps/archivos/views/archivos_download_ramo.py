from django.shortcuts import render
from ..serializers import ArchivoSerializer
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from zipfile import ZipFile

from ..models import Archivo
from ramos.models import Ramo

@api_view(["GET"])
def archivo_dl_ramo(request, ramo):
    try:
        ramo_inner  = Ramo.objects.get(sigla=ramo)
        archivos = Archivo.objects.filter(ramo=ramo_inner)
        zipObj = ZipFile(f'media/media/TEMP/{ramo}.zip', 'w')
        for f in archivos: 
            zipObj.write('media/'+str(f.path), str(f.path).split("/")[-1])
        zipObj.close()
        return JsonResponse(
            {'status':200, 
            'url': f"media/media/TEMP/{ramo}.zip"}
            , safe=False)
    except:
        return JsonResponse(
            {'status':400, 
            'url': f"media/media/TEMP/{ramo}.zip"}
            , safe=False)
