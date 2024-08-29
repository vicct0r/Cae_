from django.shortcuts import render
from usuarios.models import AlunoModel, Conta
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from rolepermissions.mixins import HasRoleMixin
from django.urls import reverse_lazy
from django.contrib import messages
from usuarios.roles import Professor

class ListagemAlunos(HasRoleMixin, ListView):
    allowed_roles = 'professor'
    template_name = 'lista_alunos.html'
    model = AlunoModel
    context_object_name = 'alunos'


class DetalheAluno(HasRoleMixin, DetailView):
    allowed_roles = 'professor'
    template_name = 'detalhe_aluno.html'
    model = AlunoModel
    context_object_name = 'aluno'


class EditarAlunoView(HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    template_name = 'editar_aluno.html'
    model = Conta
    fields = ['username', 'nome_completo']
    success_url = reverse_lazy('listagem_alunos')


class DeletarAluno(HasRoleMixin, DeleteView):
    allowed_roles = 'professor'
    model = AlunoModel
    success_url = reverse_lazy('listagem_alunos')