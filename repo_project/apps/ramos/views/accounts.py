from django.shortcuts import render
from archivos.forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password

def index(request):
    return render(request,'dappx/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    print("entro aca    ")
    
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.password = make_password(user.password)
            print("save user")
        else:
            print(user_form.errors)
        print(request.POST)
    else:
        user_form = UserForm()
    return render(request,'loginRegister/register.html')
