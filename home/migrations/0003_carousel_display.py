# Generated by Django 4.2 on 2024-12-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_carousel_options_carousel_created_on_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='display',
            field=models.BooleanField(default=False),
        ),
    ]
