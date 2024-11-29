from django.urls import path
from . import views  # Importa las vistas de la aplicación

urlpatterns = [
    path('reservas/', views.reservas, name='reservas'), 
    path('departamentos/', views.departamentos, name='departamentos'),  
    path('clientes/', views.clientes, name='clientes'),  
    path("", views.index, name="index"),
]
