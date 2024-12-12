from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.choose_articles_or_recipes, name='blog_options'),
    path('articles/', views.ArticlesList.as_view(), name='articles'),
    path('recipes/', views.RecipesList.as_view(), name='recipes'),
]