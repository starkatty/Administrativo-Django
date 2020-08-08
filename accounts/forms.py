from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django import forms

class RegisterUserForm (UserCreationForm):
    class Meta:
        models=User
        fields=[
            'username',
            'password',
        ]
        labels={
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
        }

class EditUserForm (UserCreationForm):
    class Meta:
        models=User
        fields= '__all__'
        labels={
            'username': 'Nombre de Usuario',
            'password': 'Contraseña',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Dirección de correo electrónico',
            'is_active': 'Activo',
            'is_staff': 'Es staff',
            'is_superuser': 'Es superusuario',  
        }

class RegisterGroupForm (forms.ModelForm):
    class Meta:
        models=Group
        fields= '__all__'
        labels={
            'name': 'Nombre de Grupo',
        }
