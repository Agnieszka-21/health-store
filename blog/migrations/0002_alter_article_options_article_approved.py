# Generated by Django 4.2 on 2024-12-15 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date_of_publication']},
        ),
        migrations.AddField(
            model_name='article',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
