# Generated by Django 4.2.4 on 2023-09-29 03:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0003_alter_huesped_ciudad_alter_huesped_direccion_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='huesped',
            name='habitacion',
        ),
        migrations.RemoveField(
            model_name='huesped',
            name='ingreso',
        ),
        migrations.RemoveField(
            model_name='huesped',
            name='salida',
        ),
        migrations.RemoveField(
            model_name='huesped',
            name='tarifa',
        ),
        migrations.CreateModel(
            name='Huespedxhabitacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingreso', models.DateTimeField()),
                ('salida', models.DateTimeField(blank=True, null=True)),
                ('tarifa', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('habitacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.habitacion')),
                ('huesped', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.huesped')),
            ],
        ),
    ]
