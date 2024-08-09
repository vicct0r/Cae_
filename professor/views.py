from django.shortcuts import render
from usuarios.models import Conta
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from rolepermissions.mixins import HasRoleMixin
from django.urls import reverse_lazy
from django.contrib import messages
from usuarios.roles import Professor

class ListagemAlunos(HasRoleMixin, ListView):
    allowed_roles = 'professor'
    template_name = 'lista_alunos.html'
    model = Conta
    context_object_name = 'alunos'

    def get_queryset(self):
        return Conta.objects.filter(cargo='aluno')


class DetalheAluno(HasRoleMixin, DetailView):
    allowed_roles = 'professor'
    template_name = 'detalhe_aluno.html'
    model = Conta
    context_object_name = 'aluno'


class EditarAlunoView(HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    template_name = 'editar_aluno.html'
    model = Conta
    fields = ['username', 'first_name', 'last_name', 'email']
    success_url = reverse_lazy('listagem_alunos')


class DeletarAluno(HasRoleMixin, DeleteView):
    allowed_roles = 'professor'
    model = Conta
    success_url = reverse_lazy('listagem_alunos')