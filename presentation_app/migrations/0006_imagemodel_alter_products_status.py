# Generated by Django 4.1 on 2022-10-26 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('presentation_app', '0005_alter_products_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='status',
            field=models.CharField(choices=[('a', 'موجود'), ('u', 'ناموجود')], max_length=1, verbose_name='وضعیت'),
        ),
    ]
