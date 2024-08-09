from django.shortcuts import render
from .forms import CadastroUsuarioForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from rolepermissions.roles import assign_role


class CadastroUsuarioView(CreateView):
    template_name = 'cadastro.html'
    form_class = CadastroUsuarioForm
    success_url = reverse_lazy('index')

    def form_valid(self, form, *args, **kwargs):
        response = super().form_valid(form)
        user = self.object

        if user.cargo == 'aluno':
            assign_role(user, 'aluno')
        if user.cargo == 'professor':
            assign_role(user, 'professor')
    
        return response
