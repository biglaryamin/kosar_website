# Generated by Django 3.0.4 on 2020-12-04 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20201203_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیش نویس'), ('p', 'منتشر شده')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
