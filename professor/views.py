from django.shortcuts import render
from usuarios.models import AlunoModel, Conta
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from rolepermissions.mixins import HasRoleMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from usuarios.roles import Professor

class ListagemAlunos(LoginRequiredMixin, HasRoleMixin, ListView):
    allowed_roles = 'professor'
    template_name = 'lista_alunos.html'
    model = AlunoModel
    context_object_name = 'alunos'


class DetalheAluno(LoginRequiredMixin, HasRoleMixin, DetailView):
    allowed_roles = 'professor'
    template_name = 'detalhe_aluno.html'
    model = AlunoModel
    context_object_name = 'aluno'


class EditarAlunoView(LoginRequiredMixin, HasRoleMixin, UpdateView):
    allowed_roles = 'professor'
    template_name = 'editar_aluno.html'
    model = AlunoModel
    fields = ['curso', 'turno']
    success_url = reverse_lazy('listagem_alunos')

    def form_valid(self, form):
        messages.success(self.request, 'Informações alteradas com sucesso!')
        return super().form_valid(form)


class DeletarAluno(LoginRequiredMixin, HasRoleMixin, DeleteView):
    allowed_roles = 'professor'
    model = AlunoModel
    success_url = reverse_lazy('listagem_alunos')

    def form_valid(self, form):
        messages.success(self.request, 'Usuário removido com sucesso!')
        return super().form_valid(form)