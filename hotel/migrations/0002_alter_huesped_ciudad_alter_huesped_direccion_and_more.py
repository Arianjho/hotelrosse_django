# Generated by Django 4.2.4 on 2023-09-28 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='huesped',
            name='ciudad',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='direccion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='estado_civil',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='pais',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='profesion',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='salida',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='huesped',
            name='tarifa',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
    ]