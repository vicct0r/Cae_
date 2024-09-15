from django import forms
from .models import Evento

class EventoForm(forms.ModelForm):
    class Meta:
        fields = ['nome', 'descricao', 'data', 'local', 'duracao', 'status', 'logo']


