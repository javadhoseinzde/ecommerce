from django.db import models
from app.common.models import BaseModel
# Create your models here.
class Category(BaseModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    parent = models.ForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE, verbose_name="زیر مجموعه")
    title = models.CharField(max_length=50, verbose_name="اسم")
    keywords = models.CharField(max_length=255, verbose_name="گلمه کلیدی")
    # zir_daster = models.CharField(max_length=100, blank=True, null=True, verbose_name="")
    description = models.TextField(max_length=255, verbose_name="توضیحات")
    image=models.ImageField(blank=True,upload_to='images/', verbose_name="تصویر")
    status=models.CharField(max_length=10, choices=STATUS, verbose_name="وضعیت")
    slug = models.SlugField(null=False, unique=True, verbose_name="آدرس")


    def __str__(self):
        return self.title