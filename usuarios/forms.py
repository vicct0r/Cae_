from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Aluno

class CadastroAlunoForm(UserCreationForm):
    class Meta:
        model = Aluno
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
