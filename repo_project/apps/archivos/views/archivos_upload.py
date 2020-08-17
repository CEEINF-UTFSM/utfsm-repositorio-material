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
        return Response(status=status.HTTP_400_BAD_REQUEST)
