# Generated by Django 3.0 on 2020-01-29 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chef',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Nombres')),
                ('direccion', models.TextField(max_length=200, verbose_name='Dirección')),
                ('titulo', models.TextField(max_length=200, verbose_name='Titulo')),
                ('image', models.ImageField(blank=True, null=True, upload_to='chef', verbose_name='Imagen')),
                ('facebook', models.URLField(blank=True, null=True, verbose_name='Facebook')),
                ('instagram', models.URLField(blank=True, null=True, verbose_name='Instagram')),
                ('twiter', models.URLField(blank=True, null=True, verbose_name='Twiter')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de Edición')),
            ],
            options={
                'verbose_name': 'chef',
                'verbose_name_plural': 'chefs',
                'ordering': ['name'],
            },
        ),
    ]
