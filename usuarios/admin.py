from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Conta


@admin.register(Conta)
class UsuarioAdmin(UserAdmin):
    list_display = ['username', 'first_name', 'last_name', 'email', 'cargo']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'cargo']
    ordering = ['username', 'first_name', 'last_name', 'email', 'cargo']

