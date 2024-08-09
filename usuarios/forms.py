from django.contrib.auth.forms import UserCreationForm
from .models import Conta

class CadastroUsuarioForm(UserCreationForm):
    class Meta:
        model = Conta
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'cargo']