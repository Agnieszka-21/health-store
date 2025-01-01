from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('articles/', views.ArticleListView.as_view(), name='articles'),
    path('articles/create/', views.create_article, name='create_article'),
    path('articles/<slug:slug>/', views.article_detail, name='article_detail'),
    path('articles/<slug:slug>/reading-list/', views.reading_list, name='reading_list'),

    path('articles/<int:article_id>/edit/', views.edit_article, name='edit_article'),
    path('articles/<int:article_id>/unpublish/', views.unpublish_article, name='unpublish_article'),

    path('recipes/', views.RecipeListView.as_view(), name='recipes'),
    path('recipes/create/', views.create_article, name='create_recipe'),
    path('recipes/<slug:slug>/', views.recipe_detail, name='recipe_detail'),
    path('recipes/<slug:slug>/fav-recipe-list/', views.fav_recipe_list, name='fav_recipe_list'),

    path('recipes/<int:recipe_id>/edit/', views.edit_recipe, name='edit_recipe'),
    path('recipes/<int:recipe_id>/unpublish/', views.unpublish_recipe, name='unpublish_recipe'),
    path('', views.choose_articles_or_recipes, name='blog_options'),
    
]
