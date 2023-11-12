from django.db import models

class Habitacion(models.Model):
    habitacion = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.habitacion

class Huesped(models.Model):
    dni = models.CharField(max_length=255)
    huesped = models.CharField(max_length=255)
    estado_civil = models.CharField(max_length=255, null=True, blank=True)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    ciudad = models.CharField(max_length=255, null=True, blank=True)
    pais = models.CharField(max_length=255, null=True, blank=True)
    direccion = models.CharField(max_length=255, null=True, blank=True)
    profesion = models.CharField(max_length=255, null=True, blank=True)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.huesped

class Huespedxhabitacion(models.Model):
    habitacion_rel = models.ForeignKey(Habitacion, on_delete=models.CASCADE)
    huesped_rel = models.ForeignKey(Huesped, on_delete=models.CASCADE)
    ingreso = models.DateTimeField()
    salida = models.DateField(null=True, blank=True)
    tarifa = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.huesped_rel.huesped} - {self.habitacion_rel.habitacion}"

class Usuario(models.Model):
    nombre = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    clave = models.CharField(max_length=255)
    estado = models.IntegerField(default=1)

    def __str__(self):
        return self.usuario
