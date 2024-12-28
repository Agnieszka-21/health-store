from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('events/', views.EventListView.as_view(), name='events'),
]