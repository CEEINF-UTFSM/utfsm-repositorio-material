from django.urls import path
from . import views

app_name = 'archivos'
urlpatterns = [
    path("<str:sigla>/", views.root, name="arch-root"),
    path("ajax/<str:sigla>/", views.zip_ramo, name="zip-ramo"),
    path("", views.pick_ramo, name="pick-ramo"),
    path("upload/", views.archivo_upload, name="archivos-upload"),
]
