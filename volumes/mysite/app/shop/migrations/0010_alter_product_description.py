# Generated by Django 4.0.7 on 2024-03-03 13:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=ckeditor.fields.RichTextField(verbose_name='توضیحات'),
        ),
    ]