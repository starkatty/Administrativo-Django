from django.shortcuts import render, redirect, get_object_or_404
from blog.models import *
from blog.forms import PostForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse


class PostsList(ListView):
    model=Post

class PostCreate(SuccessMessageMixin, CreateView):
    model=Post
    form=Post
    fields="__all__"
    success_message='El Post fue creado corectamente'
    def get_success_url(self):
        return reverse('listpost')

class PostDetail(DetailView):
    model=Post

class PostUpdate(SuccessMessageMixin, UpdateView):
    model=Post
    form=Post
    fields="__all__"
    success_message="El Post ha sido actualizado correctamente"
    def get_success_url(self):
        return reverse('listpost')

class PostDelete(SuccessMessageMixin, DeleteView):
    model=Post
    form=Post
    fields="__all__"
    def get_success_url(self):
        success_message='El Post fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse('listpost')

class PostDetailView(DetailView):
    model=Post
    template_name='blog/post-detail.html'

def anadepost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    form=PostForm()

    return render (request, 'blog/create-post.html', {'form':form})


def welcome(request):
    # Si estamos identificados devolvemos la portada
    if request.user.is_authenticated:
        return render(request, "blog/welcome.html")
    # En otro caso redireccionamos al login
    return redirect('/login')

   
    
def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('/blog/welcome.html')

    # Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})


def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('/')
    


