from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    #Autenticación de Usuarios 
    path('login/', SignInView.as_view(template_name="login.html"), name='login'),  
    path('login_user/', SignUpView.as_view(template_name="welcome.html"), name='Sign'),
    path('logout/', SignOutView.as_view(template_name="login.html"), name='logout'),
    path('welcome/', WelcomeView.as_view(template_name="welcome.html"), name='welcome'),
    
    
    path('userregister/', views.userregister, name='userregister'),
    path('authent_autori/', views.authent_autori, name='authent_autori'),
    
    #Usuarios
    path('user/', UserList.as_view(template_name="users.html"), name='listuser'),
    path('user/detail/<int:pk>', UserUpdate.as_view(template_name="user-detail.html"), name='userdetail'),
    path('user/create', UserCreate.as_view(template_name="register.html"), name='createuser'),
    path('user/edit/<int:pk>', PasswordUpdate.as_view(template_name="update-password.html"), name='updateuser'),
    path('user/delete/<int:pk>', UserDelete.as_view(template_name="user_confirm_delete.html"), name='deleteuser'),   
    path('user/<int:pk>', UserListSearch.as_view(template_name="users.html"), name='userlistsearch'),

    #Filtros para los usuarios
    path('user/staff', Staff.as_view(template_name="users.html"), name='staff'),
    path('user/nostaff', NoStaff.as_view(template_name="users.html"), name='nostaff'),
    path('user/superuser', Superuser.as_view(template_name="users.html"), name='superuser'),
    path('user/nosuperuser', NoSuperuser.as_view(template_name="users.html"), name='nosuperuser'),
    path('user/active', Active.as_view(template_name="users.html"), name='active'),
    path('user/noactive', NoActive.as_view(template_name="users.html"), name='noactive'),

    #Grupos
    path('groups/', GroupsList.as_view(template_name="groups.html"), name='groups'),
    path('groups/detail/<int:pk>', GroupUpdate.as_view(template_name="group-detail.html"), name='groupdetail'),
    path('groups/creategroup', GroupCreate.as_view(template_name="create-group.html"), name='creategroup'),
    path('groups/edit/<int:pk>', GroupPasswordUpdate.as_view(template_name="group-update-password.html"), name='groupupdatepassword'),
    path('groups/delete/<int:pk>', GroupDelete.as_view(template_name="group_confirm_delete.html"), name='groupdelete'),   
]
