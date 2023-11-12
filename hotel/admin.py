from django.contrib import admin
from .models import Habitacion, Huesped, Huespedxhabitacion

admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(Huespedxhabitacion)
