# Generated by Django 4.1 on 2022-10-26 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation_app', '0006_imagemodel_alter_products_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
