# Generated by Django 4.1 on 2022-11-08 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation_app', '0012_alter_textmodel_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('u', 'ناموجود'), ('a', 'موجود')], max_length=1, verbose_name='وضعیت'),
        ),
    ]