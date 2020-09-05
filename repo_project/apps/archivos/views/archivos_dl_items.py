"""
ENCARGADO DE DESCARGAR TODOS LOS ARCHIVOS ASOCIADOS A UN RAMO, 
DEVUELVE UN JSON {} CON EL ESTADO Y LA UBICACION DEL ZIP
"""
from zipfile import ZipFile
from django.http import JsonResponse
from rest_framework.decorators import api_view

from ..models import Archivo

import random, string
def get_random_str(N=20):
    return ''.join([random.choice(string.ascii_letters) for _ in range(N)])

@api_view(["POST"])
def archivo_dl_selected(request):
    try:
        random_name = get_random_str()+'.zip'
        zip_obj = ZipFile(f'media/media/TEMP/{random_name}', 'w')
        archivos = Archivo.objects.filter(id__in=request.data['files'])
        for file in archivos:
            to_dir = "/".join(str(file.path).split("/")[2:])
            zip_obj.write('media/'+str(file.path), to_dir)
        zip_obj.close()
        return JsonResponse({
            'status':200,
            'url': f"media/media/TEMP/{random_name}"})
    except:
        return JsonResponse({
            'status':400})
