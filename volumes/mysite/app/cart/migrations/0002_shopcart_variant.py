# Generated by Django 4.0.7 on 2024-01-17 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_product_data'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopcart',
            name='variant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.variants'),
        ),
    ]