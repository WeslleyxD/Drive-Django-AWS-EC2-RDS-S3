from django.contrib import admin
from django.urls import path, include
from .import views

app_name = 'drive'

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('register/', views.user_register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/<str:user>', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('delete/<str:item>', views.delete_item, name='delete_item'),
    path('download/<str:item>', views.download_item, name='download_item'),
    path('test', views.test, name='test'),
]
