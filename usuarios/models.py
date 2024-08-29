from django.db import models
from django.contrib.auth.models import AbstractUser


class Conta(AbstractUser):
    pass
    CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    cargo = models.CharField('função', max_length=10, choices=CHOICES)
    nome_completo = models.CharField('Nome Completo', max_length=40, default='')
    is_ativo = models.BooleanField('Ativo?', default=False, editable=False)
    is_funcionario = models.BooleanField('Funcionario?', default=False, editable=False)

    def __str__(self):
        return self.username


class AlunoModel(models.Model):
    CURSO_CHOICES = (
        ('BCC', 'Ciencia da Computação'),
        ('AG', 'Agronomia'),
        ('QI', 'Quimica Industrial'),
        ('ZO', 'Zootecnia'),
    )
    usuario = models.OneToOneField(Conta, on_delete=models.CASCADE)
    curso = models.CharField('Curso', max_length=3, choices=CURSO_CHOICES)

    def __str__(self):
        return f'{self.usuario.username} - {self.curso}'


class ProfessorModel(models.Model):
    ESPECIALIDADE_CHOICES = (
        ('CS', 'Ciência da Computação'),
        ('SE', 'Engenharia de Software'),
        ('AI', 'Inteligência Artificial'),
        ('DS', 'Data Science'),
        ('AG', 'Agronomia'),
        ('AP', 'Agropecuária'),
        ('AS', 'Agroecologia'),
        ('AGRO', 'Engenharia Agronômica'),
        ('ZO', 'Zootecnia'),
        ('VM', 'Medicina Veterinária'),
        ('ZOA', 'Produção Animal'),
        ('ZOA', 'Nutrição Animal'),
        ('QI', 'Química Industrial'),
        ('EQ', 'Engenharia Química'),
        ('CQ', 'Química'),
        ('MT', 'Materiais e Metalurgia'),
    )
    usuario = models.OneToOneField(Conta, on_delete=models.CASCADE)
    especialidade = models.CharField('Formação', max_length=4, choices=ESPECIALIDADE_CHOICES)

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade}'