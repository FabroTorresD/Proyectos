from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    lugarResidencia = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Reserva(models.Model):
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    cantidad_de_personas = models.IntegerField()
    departamentos = models.ManyToManyField(Departamento, related_name='reservas')
    montoTotal = models.DecimalField(max_digits=10, decimal_places=2)
    montoPagado = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Reserva de {self.cliente} del {self.fecha_inicio} al {self.fecha_fin}"
