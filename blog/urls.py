from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.welcome),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout),
    path('CambiarContrasena', views.modifidpassword),
    path('UsuarioRegistrado', views.userregister),   
]


