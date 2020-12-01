from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="archivos-home"),
    path("register/", views.register, name="page-login"),

]
