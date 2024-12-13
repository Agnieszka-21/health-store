from django.db import models
from django.utils.text import slugify 

import datetime


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    banner_img = models.ImageField(null=True, blank=True)
    img_title = models.CharField(max_length=150)
    content = models.TextField()
    keywords = models.CharField(max_length=300)
    published = models.BooleanField(default=False)
    date_of_publication = models.DateField(null=True, blank=True)
    related_products = models.ManyToManyField('products.Product', related_name='articles', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Recipe(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    banner_img = models.ImageField(null=True, blank=True)
    img_title = models.CharField(max_length=150)
    description = models.TextField()
    ingredients = models.TextField()
    method = models.TextField()
    keywords = models.CharField(max_length=300)
    published = models.BooleanField(default=False)
    date_of_publication = models.DateField(default=datetime.date.today)
    related_products = models.ManyToManyField('products.Product', related_name='recipes', blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title