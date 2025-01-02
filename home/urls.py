from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('choose_carousel/', views.choose_carousel, name='choose_carousel'),
    path('create_carousel/', views.create_carousel, name='create_carousel'),
    path('edit_carousel/<int:carousel_id>', views.edit_carousel, name='edit_carousel'),
    path('delete_carousel/<int:carousel_id>', views.delete_carousel, name='delete_carousel'),
    path('404/', views.error404, name='error404'),
    path('500/', views.error500, name='error500'),
]