# Generated by Django 4.0.2 on 2022-03-23 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_alter_article_status_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['date_added'], 'verbose_name': 'کامنت', 'verbose_name_plural': 'کامنت ها'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='article',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.article', verbose_name='مقاله'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='body',
            field=models.TextField(blank=True, null=True, verbose_name='متن'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='زمان نوشتن'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='نام'),
        ),
    ]