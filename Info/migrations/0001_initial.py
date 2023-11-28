# Generated by Django 4.2.4 on 2023-09-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MasudModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('masud_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MuntasirModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('muntasir_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='NoticeModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notice', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ParthoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partho_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RafiModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rafi_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RazzakModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razzak_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RiadulModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('riadul_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShahinModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shahin_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ShaonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shaon_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TariqulModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tariqul_not', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ZahidModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zahid_not', models.CharField(max_length=200)),
            ],
        ),
    ]