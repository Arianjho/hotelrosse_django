from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('habitaciones/', views.habitaciones, name='habitaciones'),
    path('habitaciones/update/<int:idhabitacion>/', views.habitacion_update, name='habitacion_update'),
    path('habitaciones/delete/<int:idhabitacion>/', views.habitacion_delete, name='habitacion_delete'),
    path('huespedes/', views.huespedes, name='huespedes'),
    path('huespedes/update/<int:idhuesped>/', views.huesped_update, name='huesped_update'),
    path('huespedes/delete/<int:idhuesped>/', views.huesped_delete, name='huesped_delete'),
    path('descargar_libro_huespedes', views.descargar, name='descargar_libro'),
    path('consultar_dni/<str:dni>/', views.proxy, name='consultar_dni'),
]