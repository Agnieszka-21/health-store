from django.db import models

# Copied from CI's Boutique Ado walkthrough for now

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    ingredients = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)

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
        return self.name_primary_img
        