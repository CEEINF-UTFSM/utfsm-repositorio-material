from django.shortcuts import render, redirect
from django.core import serializers
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

from ..models import Archivo
from ..forms import ArchivoForm

from ramos.models import Carrera
from ramos.models import Ramo


def archivo_upload(request):
    if request.method == "POST":
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("archivos-upload")
    else:
        form = ArchivoForm()
        carreras = Carrera.objects.defer()
        ramos = Ramo.objects.all()
    
        
        
        js_carreras = serializers.serialize('json', carreras)
        js_ramos = serializers.serialize('json', ramos)


    return render(request, "archivos/upload.html", {
        "form": form,
        'js_carreras': js_carreras,
        'js_ramos': js_ramos,
        'carreras': carreras,
        'ramos': ramos

    })
