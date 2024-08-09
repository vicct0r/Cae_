from django.db import models
from django.contrib.auth.models import AbstractUser

class Conta(AbstractUser):
    CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )
    cargo = models.CharField('função', max_length=10, choices=CHOICES)