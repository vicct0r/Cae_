from django.shortcuts import render
from .models import Emprestimo, Armario
from django.views.generic import ListView, View
from django.shortcuts import get_object_or_404, redirect

class ArmariosView(ListView):
    template_name = 'listagem_armarios.html'
    model = Armario

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # Adiciona emprestimos do usuário ao contexto
        emprestimos = Emprestimo.objects.filter(usuario=user)
        context['emprestimos'] = emprestimos
        return context


class EmprestimosView(View):
    def get(self, request, *args, **kwargs):
        armario = get_object_or_404(Armario, id=kwargs['pk'])
        emprestimo = Emprestimo.objects.create(
            usuario = request.user,
            armario = armario,
        )
        emprestimo.emprestar()
        return redirect('lista_armarios')