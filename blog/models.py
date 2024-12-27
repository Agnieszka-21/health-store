from django.db import models
from django.utils.text import slugify
from django.db.models.signals import post_save
from django.dispatch import receiver

from products.models import Product
from profiles.models import UserProfile

import datetime


class Article(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    banner_img = models.ImageField(null=True, blank=True)
    img_title = models.CharField(max_length=150)
    content = models.TextField()
    keywords = models.CharField(max_length=300)
    date_of_publication = models.DateField(null=True, blank=True)
    related_products = models.ManyToManyField(Product, related_name='articles', blank=True)
    approved = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_of_publication']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.approved and (self.date_of_publication <= datetime.date.today()):
            self.published = True
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
    date_of_publication = models.DateField(default=datetime.date.today)
    related_products = models.ManyToManyField(Product, related_name='recipes', blank=True)
    approved = models.BooleanField(default=False)
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_of_publication']

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        if self.approved and (self.date_of_publication <= datetime.date.today()):
            self.published = True
        super(Recipe, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Reading(models.Model):
    user_profile = models.OneToOneField(UserProfile, on_delete=models.CASCADE, related_name='reading_list')
    bookmarked_articles = models.ManyToManyField(Article, blank=True)


@receiver(post_save, sender=UserProfile)
def create_or_update_reading_list(sender, instance, created, **kwargs):
    """
    Create or update a personal reading list
    """
    # if created:
    Reading.objects.create(user_profile=instance)
    # Existing users: just save the wishlist
    instance.reading_list.save()
