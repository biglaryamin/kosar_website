from django.db import models
from django.utils import timezone


STATUS_CHOICES={
        ('a','موجود'),
        ('u','ناموجود'),
    }


class Products(models.Model):
    name      =models.CharField(max_length=200, verbose_name="عنوان")
    description=models.TextField(verbose_name="محتوا")
    status     =models.CharField(max_length=1 ,choices=STATUS_CHOICES, verbose_name="وضعیت")
    slug       =models.SlugField(max_length=100,unique=True, verbose_name="آدرس")
    thumbnail  =models.ImageField(upload_to="images",verbose_name="تصویر")
    publish    =models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")


    class Meta:
        verbose_name       ="محصول"
        verbose_name_plural="محصولات"
        ordering           =['-publish']
