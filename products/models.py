from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from profiles.models import UserProfile


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    url = models.URLField(max_length=180, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_url(self):
        return self.url


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Image(models.Model):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE, related_name='images')
    primary_img_url = models.URLField(max_length=1024, null=True, blank=True)
    primary_img = models.ImageField(null=True, blank=True)
    name_primary_img = models.CharField(max_length=254, null=True, blank=True)
    secondary_img_url = models.URLField(max_length=1024, null=True, blank=True)
    secondary_img = models.ImageField(null=True, blank=True)
    name_secondary_img = models.CharField(max_length=254, null=True, blank=True)
    tertiary_img_url = models.URLField(max_length=1024, null=True, blank=True)
    tertiary_img = models.ImageField(null=True, blank=True)
    name_tertiary_img = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.product.name


class Wishlist(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='wishlist')
    favourite_products = models.ManyToManyField(Product)


@receiver(post_save, sender=UserProfile)
def create_or_update_wishlist(sender, instance, created, **kwargs):
    """
    Create or update a personal wishlist
    """
#     if created:
    Wishlist.objects.create(user_profile=instance)
#     # Existing users: just save the wishlist
#     instance.wishlist.save()
