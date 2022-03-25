from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
	is_author   =models.BooleanField(default=False, verbose_name="وضعیت نویسندگی")
	special_user=models.DateTimeField(default=timezone.now, verbose_name='کاربر ویژه تا  ')
	degree      =models.CharField(max_length=20 , blank=True, null=True, verbose_name='مدرک دانشگاهی')
	job_position=models.CharField(max_length=20 , blank=True, null=True, verbose_name='موقعیت شغلی')
	thumbnail   =models.ImageField(upload_to="images", default='/img/default.jpg' , null=True, blank=True , verbose_name="تصویر")


	def is_special_user(self):
		if self.special_user > timezone.now():
			return True
		else:
			return False
	
	is_special_user.boolean=True
	is_special_user.short_description="کاربر ویژه"
