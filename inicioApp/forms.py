from django import forms
from .models import *


class Manicureform(forms.ModelForm):
    class Meta:
        model = manicure
        fields = ('id', 'id_usuario', 'fecha', 'detalle')
        labels = {
            'id': 'id:',
            'id_usuario': 'id_usuario',
            'fecha': 'fecha',
            'detalle': 'detalle'
        }


class Pedicureform(forms.ModelForm):
    class Meta:
        model = peicure
        fields = ('id', 'id_usuario', 'fecha', 'detalle')
        labels = {
            'id': 'id:',
            'id_usuario': 'id_usuario',
            'fecha': 'fecha',
            'detalle': 'detalle'
        }


class Clienteform(forms.ModelForm):
    class Meta:
        model = cliente
        fields = ('id', 'id_usuario', 'ci', 'nombre', 'apellido', 'telefono', 'email')
        labels = {
            'id': 'id:',
            'id_usuario': 'id_usuario',
            'ci': 'ci',
            'nombre': 'nombre',
            'apellido': 'apellido',
            'telefono': 'telefono',
            'email': 'email'
        }
