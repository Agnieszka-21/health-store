from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('', views.choose_articles_or_recipes, name='blog_options'),
]