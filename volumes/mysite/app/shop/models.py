from django.db import models
from app.common.models import BaseModel
from app.category.models import Category
# Create your models here.


class Product(BaseModel):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )

    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    category = models.ManyToManyField(Category, related_name="articles", verbose_name="دسته بندی") 
    title = models.CharField(max_length=150, verbose_name="اسم")
    slug = models.SlugField(null=False, unique=True, verbose_name="آدرس")
    description = models.TextField(max_length=255, verbose_name="توضیحات")
    image=models.ImageField(upload_to='images/',null=False, verbose_name="تصویر")
    price = models.DecimalField(max_digits=12, decimal_places=2,default=0, verbose_name="قیمت")
    Profit = models.DecimalField(max_digits=12, decimal_places=2, default=0, verbose_name="سود")
    variant=models.CharField(max_length=10,choices=VARIANTS, default='None', verbose_name="گونه")
    tedad_bazdid = models.IntegerField(default=0, verbose_name="تعداد بازدید")
    pishnahad = models.BooleanField(default=True, verbose_name="پیشنهاد")
    tedad_frosh = models.IntegerField(default=0, verbose_name="تعداد فروش")
    discount = models.IntegerField(default=0, verbose_name="تخفیف")
    status=models.CharField(max_length=10,choices=STATUS, verbose_name="وضعیت")
    # data = JSONField(null=True, verbose_name="دیتا")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

