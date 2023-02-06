from django.contrib import admin
from .models import *


# Register your models here.


@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ("Nome", "CPF", "Telefone", "Convênio", "Plano")

    search_fields = ['Nome']

