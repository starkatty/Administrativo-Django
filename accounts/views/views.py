# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.models import User
from accounts.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse

class UserList(ListView):
    model=User
    template_name='accounts/users.html'
    
class UserCreate(SuccessMessageMixin, CreateView):
    model=User
    form_class=RegistroUserForm
    template_name='accounts/register.html'
    fields="__all__"
    success_message='El Usuario fue creado corectamente'
    def get_success_url(self):
        return reverse('listuser')

class UserDetail(DetailView):
    model=User

class UserUpdate(SuccessMessageMixin, UpdateView):
    model=User
    form=User
    template_name='accounts/update-password.html'
    fields="__all__"
    success_message="El Usuario ha sido actualizado correctamente"
    def get_success_url(self):
        return reverse('listuser')

class UserDelete(SuccessMessageMixin, DeleteView):
    model=User
    form=User
    fields="__all__"
    def get_success_url(self):
        success_message='El Usuario fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse('listuser')

class UserDetailView(DetailView):
    model=User
    template_name='accounts/user-detail.html'

def register(request):
    return render(request, "accounts/register.html")

def registeruser(request):
    nombre_user= request.POST["nombre"]
    contrasena_user= request.POST["contrasena"]
    confirm_contrasena_user= request.POST["contrasenaconfirmacion"]
    if contrasena_user==confirm_contrasena_user:
        auth_user.username=nombre_user
        auth_user.password=contrasena_user
        auth_user.save()
        mensaje="Usuario Registrado"
    else:
        mensaje="Introduzca valores correctos"
    return render(request, "blog/register.html",{'mensaje': mensaje}) 


# Creando para modificar la Contraseña
class ModifidPassword(SuccessMessageMixin, UpdateView):
    template_name="blog/update-password.html"
    fields="__all_"
    success_message="La contraseña ha sido actualizada correctamente"
    def get_success_url(self):
        return reverse('listpost')

def modifidpassword(request):
    return render(request, "blog/update-password.html", {})

def userregister(request):
    return render(request, "blog/users-register.html", {})
  
