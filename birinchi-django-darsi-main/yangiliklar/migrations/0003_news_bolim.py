# Generated by Django 4.2.2 on 2023-06-14 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yangiliklar', '0002_news_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='bolim',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='yangiliklar.category'),
            preserve_default=False,
        ),
    ]
