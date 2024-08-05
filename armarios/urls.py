from django.urls import path
from .views import ArmariosView, EmprestimosView

urlpatterns = [
    path('', ArmariosView.as_view(), name='lista_armarios'),
    path('emprestimo/<int:pk>/', EmprestimosView.as_view(), name='emprestimo_armario'),
    
]