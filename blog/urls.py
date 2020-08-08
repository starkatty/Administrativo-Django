from django.contrib import admin
from django.urls import path
from blog.views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, PostsAdmin
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    #path('', views.login),
    #path('', views.welcome),
    #path('updatepassword/', ModifidPassword.as_view(template_name="update-password.html"), name='cambiarpassword'),
    #path('cambiar-contrasena/', views.modifidpassword, name='modifidpassword'),
    path('anade-post/', views.anadepost, name='anadepost'), 
    path('posts/', PostsList.as_view(template_name="posts.html"), name='listpost'),
    path('posts/detail/<int:pk>', PostDetail.as_view(template_name="post-detail.html"), name='detailpost'),
    path('posts/admin/', views.PostsAdmin, name='postadmin'),
    path('posts/create', PostCreate.as_view(template_name="create-post.html"), name='createpost'),
    path('posts/edit/<int:pk>', PostUpdate.as_view(template_name="post-detail.html"), name='updatepost'),
    path('posts/delete/<int:pk>', PostDelete.as_view(), name='deletepost'),   
    path('', UserCreate.as_view(template_name="register.html"), name='createuser'),
]


