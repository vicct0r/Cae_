from django.db import models
from django.contrib.auth.models import AbstractUser
from stdimage import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return f'profiles/{filename}' 


class Conta(AbstractUser):
    pass
    CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    multado = models.BooleanField('Multado', default=False)
    nome_completo = models.CharField('Nome Completo', max_length=40)
    is_ativo = models.BooleanField('Ativo?', default=False, editable=False)
    is_funcionario = models.BooleanField('Funcionario?', default=False, editable=False)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Conta'
        verbose_name_plural = 'Contas'


class AlunoModel(models.Model):
    TURNO_CHOICES = (
        ('Horário Integral', 'Horario Integral'),
        ('Noturno', 'Noturno')
    )
    CURSO_CHOICES = (
        ('BCC', 'Ciencia da Computação'),
        ('AG', 'Agronomia'),
        ('QI', 'Quimica Industrial'),
        ('ZO', 'Zootecnia'),
    )
    usuario = models.OneToOneField(Conta, on_delete=models.CASCADE)
    curso = models.CharField('Curso', max_length=3, choices=CURSO_CHOICES)
    img = StdImageField(
                        'Imagem', 
                        upload_to=get_file_path, 
                        variations={'thumb':{'width':460, 'height':460, 'crop':True}},
                        default='default/default_user.avif'
    )
    turno = models.CharField('Turno', max_length=18, choices=TURNO_CHOICES,  default='#')

    def __str__(self):
        return f'{self.usuario.username} - {self.curso}'

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'


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
    img = StdImageField(
                        'Imagem', 
                        upload_to=get_file_path, 
                        variations={'thumb':{'width':460, 'height':460, 'crop':True}},
                        default='default/default_user.avif'
    )

    def __str__(self):
        return f'{self.usuario.username} - {self.especialidade}'

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'



"""
Por algum motivo consegui fazer com que o upload de imagens funcionasse para ambos usuários;
Agora precisamos do seguinte:

-Fazer com que o professor também tenha um 'Meu_pefil'
-Fazer implementação de regra que não permite usuario de pegar mais de um armário por vez
-Fazer com que  o usuário tome multa se não devolver o armário
-Fazer a parte de atendimento do usuário
-Procurar a pasta de Registro e Login para alterar o template de ambos
-Fazer Atendimento ficar pronto e funcional para ambos os lados
-APRENDER USAR MESSAGES PARA INTEGRAR NO SITE INTEIRO
"""