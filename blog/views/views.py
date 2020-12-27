from django.shortcuts import render, redirect, get_object_or_404
from blog.models import *
from blog.forms import PostForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.http import HttpResponse

#Lista de Posts
class PostsList(ListView):
    model=Post
    template_name='posts.html'

#Crear Post  
class PostCreate(SuccessMessageMixin, CreateView):
    model=Post
    form=PostForm
    template_name='create-post.html'
    fields="__all__"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_list'] = User.objects.all()
        return context  
    def get_success_url(self):
        success_message='El Post fue creado corectamente'
        messages.success(self.request, success_message)
        return reverse_lazy('createpost')  

#Detalle del Post
class PostDetail(DetailView):
    model=Post
    template_name='post-detail.html'

#Modificar Post
class PostUpdate(SuccessMessageMixin, UpdateView):
    model=Post
    form=PostForm
    template_name='create-post.html'
    fields="__all__"
    success_message="El Post ha sido actualizado correctamente"
    def get_success_url(self):
        return reverse('listpost')

#Eliminar Post
class PostDelete(SuccessMessageMixin, DeleteView):
    model=Post
    template_name='confir_delete_post.html'
    def get_success_url(self):
        success_message='El Post fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse('listpost')

def PostsAdmin(request):
    return render (request, 'post-admin.html')
    
def anadepost(request):
    if request.method=='POST':
        form=PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post')
    form=PostForm()

    return render (request, 'create-post.html', {'form':form})





    


