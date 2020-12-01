from django import forms
from .models import Archivo
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



class ArchivoForm(forms.ModelForm):
    class Meta:
        model = Archivo
        fields = ("nombre", "ramo", "tipo", "semestre", "archivo")

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('first_name','last_name','password','email')

    def save(self, commit=True):
        user = super().save(False)
        user.username = user.email
        user.password = make_password(user.password)
        user = super().save()
        return user


    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        print(f"pass es {password} / confirm pass es {confirm_password}")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            )