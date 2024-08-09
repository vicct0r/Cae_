from django.urls import path
from .views import CadastroUsuarioView
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', CadastroUsuarioView.as_view(), name='cadastro'),
    path('login/', LoginView.as_view(template_name='login_page.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]