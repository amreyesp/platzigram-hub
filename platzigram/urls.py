
"""Platzigram urls"""
#Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


#Local
from platzigram import views as local_views
from posts import views as post_views #Estas son las vistas de la aplicación
from users import views as user_views

urlpatterns = [
    path('admin/',admin.site.urls, name='admin'),

    path('', post_views.list_posts, name = 'feed'),
    path('posts/new/', post_views.create_post, name = 'create_post'),

    path('users/login/', user_views.LoginView.as_view(), name = 'login'),
    path('users/logout/', user_views.logout_view, name = 'logout'),
    path('users/signup/', user_views.signup_view, name = 'signup'),
    path('users/me/profile/', user_views.update_profile, name = 'update_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
