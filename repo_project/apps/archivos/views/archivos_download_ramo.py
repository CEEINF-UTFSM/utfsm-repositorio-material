"""
ENCARGADO DE DESCARGAR TODOS LOS ARCHIVOS ASOCIADOS A UN RAMO, 
DEVUELVE UN JSON {} CON EL ESTADO Y LA UBICACION DEL ZIP
"""
from zipfile import ZipFile
from django.http import JsonResponse
from rest_framework.decorators import api_view


from ramos.models import Ramo
from ..models import Archivo

@api_view(["GET"])
def archivo_dl_ramo(request, ramo):
    try:
        ramo_inner = Ramo.objects.get(sigla=ramo)
        archivos = Archivo.objects.filter(ramo=ramo_inner)
        zip_obj = ZipFile(f'media/media/TEMP/{ramo}.zip', 'w')
        for file in archivos:
            to_dir = "/".join(str(file.path).split("/")[2:])
            zip_obj.write('media/'+str(file.path), to_dir)
        zip_obj.close()
        return JsonResponse(
            {'status':200,
            'url': f"media/media/TEMP/{ramo}.zip"}
            , safe=False)
    except:
        return JsonResponse(
            {'status':400}
            , safe=False)
