from django.db import models
from .paciente import Paciente
from .profissional import ProfissionalSaude

class Prontuario(models.Model):
    descricao = models.TextField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
