# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView  
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms
from django.contrib.auth.models import User, Group
from accounts.forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as do_logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import Perfil
from django.contrib.auth.hashers import make_password
#from django.conf.urls import url

#Vista para la bienvenida al usuario
class WelcomeView(TemplateView):
   template_name = 'accounts/users-register.html'

#Vista para el login
class SignInView(LoginView):
    template_name = 'accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(setting.LOGIN_REDIRECT_URL)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ingresa con tu cuenta de Usuario al Administrativo Django'
        context['register_url'] = reverse_lazy('createuser')
        return context

#Vista para el logout
class SignOutView(LogoutView):
    template_name = 'accounts/login.html'
    pass
    
#Vistas para los usuarios
#Listar los usuarios
class UserList(ListView):
    model = User
    template_name = 'accounts/users.html'
    #Falta realizar la paginación
    #paginate_by=10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_user = User.objects.all()
        context['count_user'] = total_user.count
        return context

#Crear usuario    
class UserCreate(CreateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'register.html'

    # def form_valid(self, form):
    #     c = {'form': form, }
    #     user = form.save(commit=False)
    #     # Cleaned(normalized) data
    #     password = form.cleaned_data['password']
    #     print (password)
    #     user.set_password(password)
    #     user.save()
    #     # Create User model
    #     User.objects.create(user=user)
    #     return super(UserCreate, self).form_valid(form)

    def get_success_url(self):
        success_message='El Usuario fue creado corectamente'
        messages.success(self.request, success_message)
        return reverse_lazy('createuser')

#Modificar usuario
class UserUpdate(UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'user-detail.html'
    #fields = '__all__'
    def get_success_url(self):
        success_message="El Usuario ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('userdetail')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['group_list'] = Group.objects.all()
        return context

#Modificar Password
class PasswordUpdate(UpdateView):
    model = User
    form_class = RegisterUserForm
    template_name = 'accounts/update-password.html'
    fields = "__all__"
    def get_success_url(self):
        success_message="El Password ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('listuser')

#Eliminar usuario
class UserDelete(DeleteView):
    model = User
    template_name = 'accounts/user_confirm_delete.html'
    def get_success_url(self):
        success_message='El Usuario fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse_lazy('listuser')

#Busqueda de un usuario
class UserListSearch(ListView):
    model = User
    template_name = 'accounts/users.html'
    #form_class = SearchUserForm
    #initial = {'username':' '}
    def get_queryset(self):
        #print (self.request.GET['usersearch'])
        name=self.request.GET['usersearch']
        return User.objects.filter(username=name)
    #def get(self, request, *args, **kwargs):
    #    #form=self.form_class(initial=self.initial)
    #    name=request.GET['usersearch']
    #    print (name)
    #    result=User.objects.filter(username__iexact=name)
    #    print (result)
    #    result_total=result.first()
    #    form=self.form_class(result_total)
    #    return render (request, self.template_name, {'form':form})
    #    #Falta retornar el registro del usuario para que se muestre en el listado de los usuarios
    def get_success_url(self):
        return reverse_lazy('listuser') 

#Lista de usuarios staff
class Staff (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'staff_list'
    def get_queryset(self):
        return User.objects.filter(is_staff=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('staff')

#Lista de usuarios nostaff
class NoStaff (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'nostaff_list'
    def get_queryset(self):
        return User.objects.filter(is_staff=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('nostaff')

#Lista de usuarios superuser
class Superuser (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'superuser_list'
    def get_queryset(self):
        return User.objects.filter(is_superuser=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('superuser')

#Lista de usuarios nosuperuser
class NoSuperuser (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'nosuperuser_list'
    def get_queryset(self):
        return User.objects.filter(is_superuser=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('nosuperuser')

#Lista de usuarios active
class Active (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'active_list'
    def get_queryset(self):
        return User.objects.filter(is_active=True).order_by('username')
    def get_success_url(self):
        return reverse_lazy('active')

#Lista de usuarios noactive
class NoActive (ListView):
    model = User
    template_name = 'accounts/users.html'
    context_object_name = 'noactive_list'
    def get_queryset(self):
        return User.objects.filter(is_active=False).order_by('username')
    def get_success_url(self):
        return reverse_lazy('noactive')
   
#Vistas para los grupos
#Lista de grupos
class GroupsList(ListView):
    model = Group
    template_name = 'groups.html'
    context_object_name = 'group_list'

#Crear grupo
class GroupCreate(CreateView):
    model = Group
    form_class = RegisterGroupForm
    template_name = 'create-group.html'
    def get_success_url(self):
        success_message='El Grupo fue creado corectamente'
        messages.success(self.request, success_message)
        return reverse_lazy('creategroup')

#Modificar grupo
class GroupUpdate(UpdateView):
    model = Group
    form_class = RegisterGroupForm
    template_name = 'group-detail.html'
    def get_success_url(self):
        success_message="El Grupo ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('groupdetail')

#Modificar Password del Grupo
class GroupPasswordUpdate(UpdateView):
    model = Group
    form_class = RegisterGroupForm
    template_name = 'accounts/group-update-password.html'
    def get_success_url(self):
        success_message="El Password ha sido actualizado correctamente"
        messages.success(self.request, success_message)
        return reverse_lazy('grouplist')

#Eliminar grupo
class GroupDelete(DeleteView):
    model = Group
    template_name = 'accounts/group_confirm_delete.html'
    def get_success_url(self):
        success_message='El Grupo fue eliminado correctamente'
        messages.success(self.request, (success_message))
        return reverse_lazy('grouplist')

# Modificar la Contraseña
class ModifidPassword(UpdateView):
    template_name = "blog/update-password.html"
    fields = "__all__"
    success_message="La contraseña ha sido actualizada correctamente"
    def get_success_url(self):
        return reverse_lazy('listpost')

#Registro
def userregister(request):
    return render(request, "users-register.html")

def authent_autori(request):
    return render(request, "authent_autori.html")
  
