from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conta, ProfessorModel, AlunoModel
from .forms import CadastroUsuarioForm, CadastroUsuarioChangeForm

@admin.register(AlunoModel)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso']


@admin.register(ProfessorModel)  
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'especialidade']


@admin.register(Conta)
class UsuarioContaAdmin(UserAdmin):
    add_form = CadastroUsuarioForm
    form = CadastroUsuarioChangeForm
    model = Conta
    list_display = ['username', 'nome_completo', 'is_ativo', 'cargo']




