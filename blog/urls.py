from django.contrib import admin
from django.urls import path
from blog.views import PostsList, PostDetail, PostCreate, PostUpdate, PostDelete, welcome
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.login),
    #path('', views.welcome),
    path('logout/', views.logout),
    #path('updatepassword/', ModifidPassword.as_view(template_name="update-password.html"), name='cambiarpassword'),
    #path('cambiar-contrasena/', views.modifidpassword, name='modifidpassword'),
    path('anade-post/', views.anadepost, name='anadepost'), 

    path('posts/', PostsList.as_view(template_name="blog/posts.html"), name='listpost'),
    path('posts/detail/<int:pk>', PostDetail.as_view(template_name="blog/post-detail.html"), name='detailpost'),
    path('posts/create',PostCreate.as_view(template_name="blog/create-post.html"), name='createpost'),
    path('posts/edit/<int:pk>', PostUpdate.as_view(template_name="blog/post-detail.html"), name='updatepost'),
    path('posts/delete/<int:pk>', PostDelete.as_view(), name='deletepost'),   
]


