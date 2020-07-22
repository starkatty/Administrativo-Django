from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.register),
    path('userregister/', views.userregister),
    path('registeruser/', views.registeruser),
    
    path('user/', UserList.as_view(template_name="accounts/usuarios.html"), name='listuser'),
    path('user/detalle/<int:pk>', UserDetail.as_view(template_name="accounts/user-detail.html"), name='userdetail'),
    path('user/crear',UserCreate.as_view(template_name="accounts/register.html"), name='createuser'),
    path('user/editar/<int:pk>', UserUpdate.as_view(template_name="account/update-password.html"), name='updateuser'),
    path('user/eliminar/<int:pk>', UserDelete.as_view(), name='deleteuser'),   
]
