from django.urls import path
from archivos import views

urlpatterns = [
    path("", views.home, name="archivos-home")
]
