# Generated by Django 4.0.7 on 2024-06-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_product_price_alter_variants_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='available',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default=1, max_length=10, verbose_name='موجودی'),
            preserve_default=False,
        ),
    ]
