from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.display_events, name='events'),
    path('create/', views.create_event, name='create_event'),
    path('<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('<int:event_id>/edit/', views.edit_event, name='edit_event'),
    path('<int:event_id>/register/',
         views.event_register, name='event_register'),
]
