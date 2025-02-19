# filepath: /c:/Users/Daniel/Documents/Clase/olla_chillona_django/restaurante/forms.py
from django import forms
from .models import Plato

class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ['nombre', 'descripcion', 'categoria', 'precio', 'imagen']