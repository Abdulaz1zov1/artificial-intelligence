# Generated by Django 4.2.6 on 2023-10-30 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipta', '0002_vagon_poyezd'),
    ]

    operations = [
        migrations.AddField(
            model_name='vagon',
            name='narxi',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='yonalish',
            name='davomiyligi',
            field=models.TimeField(verbose_name='Davomiyligi'),
        ),
    ]
