# Generated by Django 4.0.7 on 2023-08-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
        ('shop', '0003_alter_product_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='articles', to='category.category', verbose_name='دسته بندی'),
        ),
    ]
