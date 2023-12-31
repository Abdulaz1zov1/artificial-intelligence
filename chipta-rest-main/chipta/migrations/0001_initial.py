# Generated by Django 4.2.6 on 2023-10-30 06:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bekat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Poyezd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50, verbose_name='Nomi')),
            ],
        ),
        migrations.CreateModel(
            name='Vagon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raqami', models.CharField(max_length=50, verbose_name='Raqami')),
                ('turi', models.CharField(choices=[('U', 'Umumiy'), ('P', 'Plaskart'), ('K', 'Kupe'), ('L', 'Lux')], default='U', max_length=1, verbose_name='Turi')),
                ('joylar_soni', models.IntegerField(verbose_name='Joylar soni')),
            ],
        ),
        migrations.CreateModel(
            name='Yonalish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=50, verbose_name='Nomi')),
                ('jonash_vaqti', models.DateTimeField()),
                ('davomiyligi', models.DateTimeField()),
                ('poyezd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chipta.poyezd', verbose_name='Poyezd')),
                ('qayerdan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qayerdan', to='chipta.bekat', verbose_name='Qayerdan')),
                ('qayerga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='qayerga', to='chipta.bekat', verbose_name='Qayerga')),
            ],
        ),
    ]
