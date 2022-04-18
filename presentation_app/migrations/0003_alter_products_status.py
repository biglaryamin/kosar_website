# Generated by Django 4.0.2 on 2022-04-18 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation_app', '0002_alter_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('u', 'ناموجود'), ('a', 'موجود')], max_length=1, verbose_name='وضعیت'),
        ),
    ]