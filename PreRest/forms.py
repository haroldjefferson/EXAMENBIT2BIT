from dataclasses import fields
from django import forms
from.models import Preguntas, Respuesta

class PreguntasForm(forms.ModelForm):
    class Meta:
        model = Preguntas
        fields = ('titulo', 'descripcion') 

class Respoderform(forms.ModelForm):
    class Meta:
        model = Respuesta
        fields = ['descripcion']

