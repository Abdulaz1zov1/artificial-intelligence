# Generated by Django 4.2.6 on 2023-11-06 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chipta', '0005_chipta_vagon_alter_chipta_yonalish'),
    ]

    operations = [
        migrations.AddField(
            model_name='chipta',
            name='joy_raqami',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
