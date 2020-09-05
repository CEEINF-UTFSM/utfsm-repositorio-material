from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage

from ..models import Archivo
from ..forms import ArchivoForm


def archivo_upload(request):
    if request.method == "POST":
        form = ArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("archivos-upload")
    else:
        form = ArchivoForm()
    # print(form)
    return render(request, "archivos/aux_upload.html", {
        "form": form
    })
