from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conta, ProfessorModel, AlunoModel
from .forms import CadastroUsuarioForm, CadastroUsuarioChangeForm


class AlunoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'curso']


class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'especialidade']


class UsuarioContaAdmin(UserAdmin):
    add_form = CadastroUsuarioForm
    form = CadastroUsuarioChangeForm
    model = Conta
    list_display = ['username', 'nome_completo', 'is_ativo', 'cargo']


admin.site.register(Conta, UsuarioContaAdmin)
admin.site.register(AlunoModel, AlunoAdmin)
admin.site.register(ProfessorModel, ProfessorAdmin)


