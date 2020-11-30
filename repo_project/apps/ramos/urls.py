from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="archivos-home"),
    path("login", views.login, name="page-login"),
    path("register", views.register, name="page-register"),

]
