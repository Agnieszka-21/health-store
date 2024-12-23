# Generated by Django 4.2 on 2024-12-12 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0003_brand_product_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('ingredients', models.TextField()),
                ('method', models.TextField()),
                ('keywords', models.CharField(max_length=300)),
                ('published', models.BooleanField(default=False)),
                ('date_of_publication', models.DateField(default=datetime.date.today)),
                ('related_products', models.ManyToManyField(blank=True, related_name='recipes', to='products.product')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('banner_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('img_title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('keywords', models.CharField(max_length=300)),
                ('published', models.BooleanField(default=False)),
                ('date_of_publication', models.DateField(blank=True, null=True)),
                ('related_products', models.ManyToManyField(blank=True, related_name='articles', to='products.product')),
            ],
        ),
    ]
