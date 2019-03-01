
"""Platzigram urls"""
#Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


#Local
from posts import views as post_views #Estas son las vistas de la aplicación
from users import views as user_views

urlpatterns = [
    path('admin/',admin.site.urls, name='admin'),

    path('', post_views.ListPosts.as_view(), name = 'feed'),
    path('posts/new/', post_views.CreatePostView.as_view(), name = 'create_post'),

    path('users/login/', user_views.LoginView.as_view(), name = 'login'),
    path('users/logout/', user_views.LogoutView.as_view(), name = 'logout'),
    path('users/signup/', user_views.SignupView.as_view(), name = 'signup'),
    path('users/me/profile/', user_views.UpdateProfileView.as_view(), name = 'update_profile'),
    path('users/<str:username>/', user_views.DetailUserView.as_view(), name = 'detail_user'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
