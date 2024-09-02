from usuarios.models import AlunoModel, ProfessorModel
from django import forms

class AlunoUpdateForm(forms.ModelForm):
    class Meta:
        model = AlunoModel
        fields = ['img']


class ProfessorUpdateForm(forms.ModelForm):
    class Meta:
        model = ProfessorModel
        fields = ['img', 'especialidade']