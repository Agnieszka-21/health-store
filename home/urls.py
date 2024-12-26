from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('choose_carousel/', views.choose_carousel, name='choose_carousel'),
    path('create_carousel/', views.create_carousel, name='create_carousel'),
]