# Generated by Django 3.0.4 on 2020-11-03 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20201103_1654'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ManyToManyField(to='blog.Category', verbose_name='دسته بندی'),
        ),
    ]
