from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('<int:product_id>/add-to-wishlist/', views.add_to_wishlist, name='add_to_wishlist'),
    path('<int:product_id>/edit-review/<int:review_id>/', views.edit_review, name='edit_review'),
    path('<int:product_id>/delete-review/<int:review_id>/', views.delete_review, name='delete_review'),
    path('manage_reviews/', views.manage_reviews, name='manage_reviews'),
]
