# Generated by Django 4.0.7 on 2023-11-15 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_slider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to='media/images/', verbose_name='تصویر'),
        ),
    ]
