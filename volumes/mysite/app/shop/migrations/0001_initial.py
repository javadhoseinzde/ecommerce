# Generated by Django 4.0.7 on 2023-08-03 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='اسم')),
                ('slug', models.SlugField(unique=True, verbose_name='آدرس')),
                ('description', models.TextField(max_length=255, verbose_name='توضیحات')),
                ('image', models.ImageField(upload_to='images/', verbose_name='تصویر')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='قیمت')),
                ('Profit', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='سود')),
                ('variant', models.CharField(choices=[('None', 'None'), ('Size', 'Size'), ('Color', 'Color'), ('Size-Color', 'Size-Color')], default='None', max_length=10, verbose_name='گونه')),
                ('tedad_bazdid', models.IntegerField(default=0, verbose_name='تعداد بازدید')),
                ('pishnahad', models.BooleanField(default=True, verbose_name='پیشنهاد')),
                ('tedad_frosh', models.IntegerField(default=0, verbose_name='تعداد فروش')),
                ('discount', models.IntegerField(default=0, verbose_name='تخفیف')),
                ('status', models.CharField(choices=[('True', 'True'), ('False', 'False')], max_length=10, verbose_name='وضعیت')),
            ],
        ),
    ]
