# Generated by Django 4.0.8 on 2022-11-16 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0003_crawledarticle_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledarticle',
            name='source',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='منبع'),
        ),
    ]
