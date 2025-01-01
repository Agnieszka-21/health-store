from django.urls import path

from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:article_id>/remove-article-bookmark/', views.remove_article_bookmark, name='remove_article_bookmark'),
    path('<int:recipe_id>/remove-recipe-bookmark/', views.remove_recipe_bookmark, name='remove_recipe_bookmark'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
    path('wishlist_items/', views.wishlist_items, name='wishlist_items'),
    path('wishlist_items/<int:product_id>/remove/', views.remove_from_wishlist, name='remove_from_wishlist'),
]
