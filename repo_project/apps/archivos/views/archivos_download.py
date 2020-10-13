"""
VISTA PARA ARCHIVOS APROBADOS, FORM PARA SELECCIONAR CUALES METER A UN .ZIP
"""
# from django.http import HttpResponse
from zipfile import ZipFile
from random import sample
from django.http import JsonResponse

from django.shortcuts import render
from ..models import Archivo
from ramos.models import Ramo

def root(request, sigla):
    all_files = Archivo.objects.filter(aceptado=True)
    all_ramos = Ramo.objects.all()
    selected_ramo = Ramo.objects.get(sigla=sigla)
    all_files = all_files.filter(ramo=selected_ramo)
    context = {
        'files': all_files,
        'ramos': all_ramos,
        'current': sigla,
        'zip': None,
    }
    if request.method == 'POST':
        print(u"\u001b[32m")
        filename = ''.join(sample("abcd", 4))
        archivos = all_files.filter(id__in=request.POST.getlist('files'))
        zip_obj = ZipFile(f'media/temp/{filename}.zip', 'w')
        for e in archivos:
            zip_obj.write('media/'+str(e.archivo), str(e.archivo))
        zip_obj.close()
        context['zip'] = '/media/temp/'+filename+".zip"
    # return render(request, 'archivos/listado.html', context)
    return render(request, 'archivos/listado.html', context)


def zip_ramo(request, sigla):
    zip_obj = ZipFile(f'media/zips/{sigla}.zip', 'w')
    all_files = Archivo.objects.filter(aceptado=True)
    selected_ramo = Ramo.objects.get(sigla=sigla)
    all_files = all_files.filter(ramo=selected_ramo)
    for e in all_files:
        zip_obj.write('media/'+str(e.archivo), str(e.archivo))
    zip_obj.close()
    return JsonResponse({'link': f'media/zips/{sigla}.zip'})


def pick_ramo(request):
    all_ramos = Ramo.objects.all()
    context = {
        'ramos': all_ramos
    }
    return render(request, 'archivos/pick.html', context)
    

