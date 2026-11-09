from django.contrib import admin
from .models import Paciente

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'idade', 'sexo', 'cpf', 'estado_civil', 'religiao', 'endereco', 'cidade', 'estado', 'telefone')
    search_fields = ('nome', 'cpf', 'cidade', 'estado')
