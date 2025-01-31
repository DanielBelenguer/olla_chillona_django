from django.db import models

# Create your models here.

class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    saldo = models.DecimalField(max_digits=5, decimal_places=2)

class Camarero(models.Model):
    nombre = models.CharField(max_length=50)


