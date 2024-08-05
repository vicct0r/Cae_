from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import CadastroAlunoView, GerenciarAlunos, DetalheAlunos, EditarAlunos, RemoverAlunos

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('cadastro/', CadastroAlunoView.as_view(), name='cadastro_aluno'),
    path('listagem_alunos/', GerenciarAlunos.as_view(), name='admin_alunos'),
    path('detalhe_aluno/<int:pk>/', DetalheAlunos.as_view(), name='admin_detalhes'),
    path('editar_aluno/<int:pk>/', EditarAlunos.as_view(), name='admin_edit'),
    path('remover_aluno/<int:pk>/', RemoverAlunos.as_view(), name='admin_remover')
]