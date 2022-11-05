# python import(s)
import os

# django import(s)
from django.db import models
from django.utils import timezone
from django.urls import reverse

# image import(s)
import PIL
from io import BytesIO
from PIL import Image
from django.core.files import File



STATUS_CHOICES={
        ('a','موجود'),
        ('u','ناموجود'),
    }



def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format("something", ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)



class Products(models.Model):
    name      =models.CharField(max_length=200, verbose_name="عنوان")
    description=models.TextField(verbose_name="محتوا")
    status     =models.CharField(max_length=1 ,choices=STATUS_CHOICES, verbose_name="وضعیت")
    slug       =models.SlugField(max_length=100,unique=True, verbose_name="آدرس")
    thumbnail  =models.ImageField(upload_to="images",verbose_name="تصویر")
    publish    =models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")


    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصولات"
        ordering = ['-publish']



class ImageModel(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    image = models.ImageField(upload_to=path_and_rename, null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
   

    def valid_extension(self,_img):
        if '.jpg' in _img:
            return "JPEG"
        elif '.jpeg' in _img:
            return "JPEG"
        elif '.png' in _img:
            return "PNG"


    # def get_absolute_url(self):
    #     return f"/images/{self.name}/"


    def get_absolute_url(self):
        return str(self.image.url)



    class Meta:
        verbose_name = "عکس"
        verbose_name_plural = "عکس ها"


class TextModel(models.Model):
    name = models.CharField(max_length=10, null=True, blank=True)
    pre_text = models.TextField(null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    post_text = models.TextField(null=True, blank=True)


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "متن"
        verbose_name_plural = "متن ها"