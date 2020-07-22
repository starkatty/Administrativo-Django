from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroUserForm (UserCreationForm):
    class Meta:
        models=User
        fields=[
            'username',
            'firtsname',
            'last_name',
            'email',
        ]
        labels={
            'username': 'Nombre de Usuario',
            'firtsname': 'Nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
        }