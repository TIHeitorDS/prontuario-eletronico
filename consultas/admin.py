from django.contrib import admin

from .models import Consulta, Diagnostico, Prescricao, Sintoma


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'data', 'horario', 'descricao')
    list_filter = ('data',)
    search_fields = ('paciente__nome', 'descricao')


@admin.register(Sintoma)
class SintomaAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'descricao')


@admin.register(Diagnostico)
class DiagnosticoAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'descricao')


@admin.register(Prescricao)
class PrescricaoAdmin(admin.ModelAdmin):
    list_display = ('consulta', 'medicamento', 'dosagem')
    search_fields = ('medicamento',)
