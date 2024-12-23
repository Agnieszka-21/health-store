# Generated by Django 4.2 on 2024-11-22 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_sizes',
        ),
        migrations.AddField(
            model_name='product',
            name='ingredients',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=6, null=True),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primary_img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('primary_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_primary_img', models.CharField(blank=True, max_length=254, null=True)),
                ('secondary_img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('secondary_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_secondary_img', models.CharField(blank=True, max_length=254, null=True)),
                ('tertiary_img_url', models.URLField(blank=True, max_length=1024, null=True)),
                ('tertiary_img', models.ImageField(blank=True, null=True, upload_to='')),
                ('name_tertiary_img', models.CharField(blank=True, max_length=254, null=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='products.product')),
            ],
        ),
    ]
