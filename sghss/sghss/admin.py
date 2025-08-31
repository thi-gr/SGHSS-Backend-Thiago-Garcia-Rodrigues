from django.contrib import admin
from .models import (
    Paciente,
    ProfissionalSaude,
    Administrador,
    Consulta,
    Receita,
    Prontuario,
    Leito
)

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'data_nascimento')
    search_fields = ('nome',)

@admin.register(ProfissionalSaude)
class ProfissionalSaudeAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especialidade')
    search_fields = ('nome', 'especialidade')
    list_filter = ('especialidade',)

@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')
    search_fields = ('nome',)

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'profissional', 'data')
    list_filter = ('data', 'profissional')
    search_fields = ('paciente__nome', 'profissional__nome')

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('id', 'consulta', 'descricao')
    search_fields = ('descricao',)

@admin.register(Prontuario)
class ProntuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'profissional', 'descricao')
    search_fields = ('descricao', 'paciente__nome', 'profissional__nome')

@admin.register(Leito)
class LeitoAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero', 'ocupado', 'administrador')
    list_filter = ('ocupado',)
    search_fields = ('numero',)
