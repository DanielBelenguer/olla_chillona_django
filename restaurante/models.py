from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    CLIENTE = 'cliente'
    CAMARERO = 'camarero'
    COCINERO = 'cocinero'
    JEFE = 'jefe'
    ROLES = [
        (CLIENTE, 'cliente'),
        (CAMARERO, 'camarero'),
        (COCINERO, 'cocinero'),
        (JEFE, 'jefe')
    ]
    usuario = models.CharField(max_length=15)
    nombre = models.CharField(max_length=25)
    apellidos = models.CharField(max_length=50)
    num_telefono = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    rol = models.CharField(max_length=10, choices=ROLES, default=CLIENTE)


class Plato(models.Model):
    CARNE = 'carne'
    PESCADO = 'pescado'
    VEGETARIANO = 'vegetariano'
    PIZZA = 'pizza'
    CATEGORIA = [
        (CARNE, 'carne'),
        (PESCADO, 'pescado'),
        (VEGETARIANO, 'vegetariano'),
        (PIZZA, 'pizza')
    ]
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIA)
    precio = models.DecimalField(max_digits=5, decimal_places=2)


class Descuento(models.Model):
    nombre = models.CharField(max_length=50)
    porcent = models.IntegerField(default=0)

class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.IntegerField()
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)