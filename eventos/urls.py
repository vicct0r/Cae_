from django.urls import path
from .views import EventoListView, EventoDetailView, EventoCreateView, EventoEditView

urlpatterns = [
    path('admin/', EventoListView.as_view(), name='evento_admin'),
    path('detalhe/<int:pk>/', EventoDetailView.as_view(), name='evento_detalhe'),
    path('admin/edit_<int:pk>/', EventoEditView.as_view(), name='evento_edit'),
    path('admin/create_event/', EventoCreateView.as_view(), name='evento_create')

]