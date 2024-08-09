from django.urls import path
from .views import ListagemAlunos, DetalheAluno, EditarAlunoView, DeletarAluno

urlpatterns = [
    path('', ListagemAlunos.as_view(), name='listagem_alunos'),
    path('detalhe/aluno_<int:pk>/', DetalheAluno.as_view(), name='detalhe_aluno'),
    path('editar/aluno_<int:pk>/', EditarAlunoView.as_view(), name='editar_aluno'),
    path('delete/aluno_<int:pk>/', DeletarAluno.as_view(), name='deletar_aluno')
]