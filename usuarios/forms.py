from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Conta, AlunoModel, ProfessorModel


class CadastroUsuarioForm(UserCreationForm):
    class Meta:
        model = Conta
        fields = ['username','nome_completo', 'password1', 'password2', 'cargo']


class CadastroUsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Conta
        fields = ['username', 'nome_completo']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('password')  # Remove o campo de senha

class AlunoForm(forms.ModelForm):
    class Meta:
        model = AlunoModel
        fields = ['img', 'curso', 'turno']


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = ProfessorModel
        fields = ['img', 'especialidade']
