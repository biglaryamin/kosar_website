# Generated by Django 4.1 on 2022-11-08 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crawler', '0002_crawledarticle_created_alter_crawledarticle_text_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledarticle',
            name='link',
            field=models.URLField(blank=True, null=True),
        ),
    ]