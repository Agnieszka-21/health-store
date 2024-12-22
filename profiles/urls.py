from django.urls import path

from . import views
from products.views import remove_from_wishlist


urlpatterns = [
    path('', views.profile, name='profile'),
    path('<int:product_id>/remove-from-wishlist/', remove_from_wishlist, name='remove_from_wishlist'),
    path('order_history/<order_number>/', views.order_history, name='order_history'),
]
