# Generated by Django 4.2.2 on 2023-06-15 13:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yangiliklar', '0003_news_bolim'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='createt_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='news',
            name='createt_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
