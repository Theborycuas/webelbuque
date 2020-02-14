# Generated by Django 3.0 on 2020-01-27 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='menu',
            options={'ordering': ['name'], 'verbose_name': 'menu', 'verbose_name_plural': 'menus'},
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.FloatField(default=0, verbose_name='Precio'),
            preserve_default=False,
        ),
    ]
