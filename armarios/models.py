from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Armario(models.Model):
    chave_string = models.CharField('Chave do Armário', max_length=6)
    disponivel = models.BooleanField('Disponivel', default=True)

    def __str__(self):
        return self.chave_string

class Emprestimo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    armario = models.ForeignKey(Armario, on_delete=models.CASCADE)
    data_emprestimo = models.DateTimeField('Data do Emprestimo', null=True, blank=True)
    data_devolucao = models.DateTimeField('Data de Devolução', null=True, blank=True)

    def __str__(self):
        return f'Armário: {self.id} -- Aluno: {self.usuario.first_name}'

    def emprestar(self):
        self.armario.disponivel = False
        self.data_emprestimo = timezone.now()
        self.armario.save()
        self.save()


    def devolver(self):
        self.armario.disponivel = True
        self.data_devolucao = timezone.now()
        self.armario.save()
        self.save()

