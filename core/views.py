from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, UpdateView, DetailView
from usuarios.forms import CadastroUsuarioChangeForm
from rolepermissions.mixins import HasRoleMixin
from django.urls import reverse, reverse_lazy
from usuarios.models import ProfessorModel, AlunoModel, Conta
from .forms import ProfessorUpdateForm, AlunoUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(TemplateView):
    template_name = 'index.html'


class MyProfileView(LoginRequiredMixin, DetailView):
    template_name = 'my_profile.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        print(user.is_funcionario)
        if user.cargo == 'professor':
            profile = ProfessorModel.objects.get(usuario=user)
        else:
            profile = AlunoModel.objects.get(usuario=user)
    
        context['profile'] = profile
        return context

    def get_object(self):
        return self.request.user


class MyAccountUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'my_account_update.html'
    form_class = CadastroUsuarioChangeForm

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Informações da conta alteradas com sucesso!')
        return super().form_valid(form)
    
    def get_success_url(self):
        # Obtenha o pk do usuário atualizado
        user_pk = self.object.pk
        return reverse('my_profile', kwargs={'pk': user_pk})


class MyProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'my_profile_update.html'
    success_url = reverse_lazy('my_profile')
    # form_class está fora desta parte pois eu preciso de uma condição para escolher o formulário.

    def get_form_class(self):
        user = self.request.user

        # fazendo os dois retornos possíveis de formulário
        if user.cargo == 'professor':
            return ProfessorUpdateForm
        return AlunoUpdateForm

    def get_object(self):
        user = self.request.user # retornando o usuario logado

        # especificando o usuário correto para alteração dos dados
        if user.cargo == 'professor':
            return ProfessorModel.objects.get(usuario=user)
        return AlunoModel.objects.get(usuario=user)

        # get(usuario=user) permite com que eu encontre o usuário correto dentro do meu perfil;
        # a lógica funciona desta forma porque eu fiz com que usuario fosse uma composição de perfil,
        # desta forma eu consigo encontrar o objeto relacionado com a conta de usuario sem nenhum problema.

    def form_valid(self, form):
        messages.success(self.request, 'Informações de perfil alterados com sucesso!')
        return super().form_valid(form)

    def get_success_url(self):
        user_pk = self.object.pk
        return reverse('my_profile', kwargs={'pk': user_pk})