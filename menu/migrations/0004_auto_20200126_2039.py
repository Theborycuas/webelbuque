# Generated by Django 3.0 on 2020-01-27 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_auto_20200126_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Precio'),
        ),
    ]
