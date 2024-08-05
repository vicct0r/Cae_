from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .forms import CadastroAlunoForm
from django.urls import reverse_lazy
from .roles import Aluno #Esquece de importar isso mais não se faz favor
from rolepermissions.roles import assign_role


class CadastroAlunoView(CreateView):
    template_name = 'cadastro_aluno.html'
    form_class = CadastroAlunoForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        resposta = super().form_valid(form)
        user = self.object
        assign_role(user, 'aluno')
        return resposta

#---------------------------------------#
#      Parte de gerência dos alunos     #
#---------------------------------------#
class GerenciarAlunos(ListView):
    template_name = 'gerencia_alunos.html'
    model = Aluno


class DetalheAlunos(DetailView):
    template_name = 'detalhe_alunos.html'
    model = Aluno


class EditarAlunos(UpdateView):
    template_name = 'editar_alunos.html'
    model = Aluno
    fields = ['username', 'email', 'first_name', 'last_name']
    success_url = reverse_lazy('admin_alunos')


class RemoverAlunos(DeleteView):
    template_name = 'remover_alunos.html'
    model = Aluno
    success_url = reverse_lazy('admin_alunos')