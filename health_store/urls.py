"""
health_store URL Configuration

"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import handler404


urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('basket/', include('basket.urls')),
    path('blog/', include('blog.urls')),
    path('checkout/', include('checkout.urls')),
    path('events/', include('events.urls')),
    path('products/', include('products.urls')),
    path('profile/', include('profiles.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'health_store.views.handler404'
handler500 = 'health_store.views.handler500'
