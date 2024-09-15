from django.contrib import admin
from .models import Evento 

@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    fields = ['nome', 'data', 'local', 'status']