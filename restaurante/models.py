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
    saldo = models.IntegerField(default=0)
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
    imagen = models.ImageField(upload_to='img_platos/' , null=True, blank=True)

    def __str__(self):
        return self.nombre


class Descuento(models.Model):
    nombre = models.CharField(max_length=50)
    porcent = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre

class Reserva(models.Model):
    fecha = models.DateField()
    hora = models.TimeField()
    num_personas = models.IntegerField()
    usuario = models.ForeignKey(UsuarioPersonalizado, on_delete=models.CASCADE)

    def __str__(self):
        return self.fecha

class Menu(models.Model):
    nombre = models.CharField(max_length=200)
    platos = models.ManyToManyField(Plato)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self):
        return self.nombre