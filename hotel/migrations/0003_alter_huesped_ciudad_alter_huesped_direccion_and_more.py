# Generated by Django 4.2.4 on 2023-09-28 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0002_alter_huesped_ciudad_alter_huesped_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='ciudad',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='direccion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='estado_civil',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='pais',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='profesion',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='salida',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='tarifa',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True),
        ),
    ]
