from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Perfil

#Formulario de Autenticación del Usuario
class AuthenticationUserForm (AuthenticationForm):
    first_name = forms.CharField(max_length=140, required=True, label='Nombres')
    last_name = forms.CharField(max_length=140, required=False, label='Apellidos')
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )

        labels={
            'username': 'Nombre de Usuario',
            'email': 'Dirección de Correo',
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'password1': 'Contraseña',
            'password2': 'Confirmación de Contraseña',
        } 

#Formulario para Registrar al Usuario
class RegisterUserForm (UserCreationForm):
    first_name = forms.CharField(max_length=140, required=True, label='Nombres:')
    last_name = forms.CharField(max_length=140, required=False, label='Apellidos:')
    email = forms.EmailField(required=True, label='Correo Electrónico:')

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'last_login',
            'date_joined',
            'is_active',
            'is_staff',
            'is_superuser',
        )
        labels={
            'username': 'Nombre de Usuario:',
            'email': 'Dirección de Correo:',
            'first_name': 'Nombres:',
            'last_name': 'Apellidos:',
            'password1': 'Contraseña:',
            'password2': 'Confirmación de Contraseña:',
            'last_login': 'Ultimo inicio de sesión:',
            'date_joined': 'Fecha de Alta:',
            'is_active': 'Activo:',
            'is_staff': 'Es Staff:',
            'is_superuser': 'Es Superusuario:',
        }   

#Formulario para editar el Usuario
class EditUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = '__all__'
        labels = {
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Dirección de correo electrónico',
            'is_active': 'Activo',
            'is_staff': 'Es staff',
            'is_superuser': 'Es superusuario',  
        }

#Formulario para el registro del Grupo
class RegisterGroupForm (forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        labels = {
            'name': 'Nombre de Grupo',
        }
        
#Formulario de Busqueda del Usuario
class SearchUserForm (forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'username',
        )
        
        labels={
            'name': 'Nombre de Usuario',
        }