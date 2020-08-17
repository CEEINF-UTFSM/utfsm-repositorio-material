from django.urls import path
from . import views

urlpatterns = [
    path("list/", views.archivo_list, name="archivos-list"),
    path("upload/", views.archivo_upload, name="archivos-upload")
]
