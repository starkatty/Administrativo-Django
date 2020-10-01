# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.models import User, Group
from accounts.forms import *
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

#Vista para el login del usuario
class Login(LoginRequiredMixin, View):
    model=User
    form=RegisterUserForm
    login_url='accounts/login.html'
    redirect_field_name='redirect_to'
    template_name='accounts/login.html'
    fields=[
            'username',
            'password',
        ]
    def get_success_url(self):
        return reverse_lazy('welcome')

#Vistas para los usuarios

#Listar los usuarios
class UserList(ListView):
    model=User
    template_name='accounts/users.html'
    #paginate_by=10

#Crear usuario    
class UserCreate(SuccessMessageMixin, CreateView):
    model=User
    form=RegisterUserForm
    template_name='register.html'
    fields=[
            'username',
            'password',
        ]
    def get_success_url(self):
        success_message='El Usuario fue creado corectamente'
        messages.success(self.request, success_message)
        return reverse_lazy('createuser')

#Modificar usuario
class UserUpdate(SuccessMessageMixin, UpdateView):
    model=User
    form=EditUserForm
    template_name='user-detail.html'
    fields= '__all__'
    def get_success_url(self):
        success_message="El Usuario ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('userdetail')

#Modificar Password
class PasswordUpdate(SuccessMessageMixin, UpdateView):
    model=User
    form=RegisterUserForm
    template_name='accounts/update-password.html'
    fields="__all__"
    def get_success_url(self):
        success_message="El Password ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('listuser')

#Modificar usuario
class UserDelete(SuccessMessageMixin, DeleteView):
    model=User
    template_name='accounts/user_confirm_delete.html'
    def get_success_url(self):
        success_message='El Usuario fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse_lazy('listuser')

#Busqueda de usuario
class UserListSearch(ListView):
    model=User
    template_name='accounts/users.html'

#Lista de usuarios staff
class Staff (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='staff_list'
    def get_queryset(self):
        return User.objects.filter(is_staff=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('staff')

#Lista de usuarios nostaff
class NoStaff (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='nostaff_list'
    def get_queryset(self):
        return User.objects.filter(is_staff=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('nostaff')

#Lista de usuarios superuser
class Superuser (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='superuser_list'
    def get_queryset(self):
        return User.objects.filter(is_superuser=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('superuser')

#Lista de usuarios nosuperuser
class NoSuperuser (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='nosuperuser_list'
    def get_queryset(self):
        return User.objects.filter(is_superuser=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('nosuperuser')

#Lista de usuarios active
class Active (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='active_list'
    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('active')

#Lista de usuarios noactive
class NoActive (ListView):
    model=User
    template_name='accounts/users.html'
    context_object_name='noactive_list'
    def get_queryset(self):
        return User.objects.filter(is_active=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('noactive')
   
#Vistas para los grupos
#Lista de grupos
class GroupsList(ListView):
    model=Group
    template_name='groups.html'

#Crear grupo
class GroupCreate(SuccessMessageMixin, CreateView):
    model=Group
    form=RegisterGroupForm
    template_name='create-group.html'
    fields=[
            'name',
        ]
    def get_success_url(self):
        success_message='El Grupo fue creado corectamente'
        messages.success(self.request, success_message)
        return reverse_lazy('creategroup')

#Modificar grupo
class GroupUpdate(SuccessMessageMixin, UpdateView):
    model=Group
    form=RegisterGroupForm
    template_name='group-detail.html'
    fields= '__all__'
    def get_success_url(self):
        success_message="El Grupo ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('groupdetail')

#Modificar Password del Grupo
class GroupPasswordUpdate(SuccessMessageMixin, UpdateView):
    model=Group
    form=RegisterGroupForm
    template_name='accounts/group-update-password.html'
    fields="__all__"
    def get_success_url(self):
        success_message="El Password ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('grouplist')

#Eliminar grupo
class GroupDelete(SuccessMessageMixin, DeleteView):
    model=Group
    template_name='accounts/group_confirm_delete.html'
    def get_success_url(self):
        success_message='El Grupo fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse_lazy('grouplist')

# Modificar la Contraseña
class ModifidPassword(SuccessMessageMixin, UpdateView):
    template_name="blog/update-password.html"
    fields="__all_"
    success_message="La contraseña ha sido actualizada correctamente"
    def get_success_url(self):
        return reverse_lazy('listpost')

#Registro
def register(request):
    return render(request, "accounts/register.html")

#Logout
def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')

#Welcome
def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')


'''
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

def modifidpassword(request):
    return render(request, "blog/update-password.html", {})

'''
def userregister(request):
    return render(request, "users-register.html")

def authent_autori(request):
    return render(request, "authent_autori.html")
  
