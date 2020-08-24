<<<<<<< HEAD
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
    print(form)
    return render(request, "archivos/aux_upload.html", {
        "form": form
    })
=======
from django.shortcuts import render
from ..serializers import ArchivoSerializer
from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import Archivo


@api_view(["POST"])
def archivo_upload(request):

    serializer = ArchivoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        print(serializer.errors)
        print(request.data)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
>>>>>>> 625f8cf36533629d9ef0062ae7f147b017a48f21
