# Generated by Django 4.0.2 on 2022-03-26 11:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='عنوان')),
                ('description', models.TextField(verbose_name='محتوا')),
                ('status', models.CharField(choices=[('u', 'ناموجود'), ('a', 'موجود')], max_length=1, verbose_name='وضعیت')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='آدرس')),
                ('thumbnail', models.ImageField(upload_to='images', verbose_name='تصویر')),
                ('publish', models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار')),
            ],
            options={
                'verbose_name': 'محصول',
                'verbose_name_plural': 'محصولات',
                'ordering': ['-publish'],
            },
        ),
    ]