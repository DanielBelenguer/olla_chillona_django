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
    rol = models.CharField(max_length=10, choices=ROLES, default=CLIENTE)



class Plato(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()
    categoria = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=5, decimal_places=2)



