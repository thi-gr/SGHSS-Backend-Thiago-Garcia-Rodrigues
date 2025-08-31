from django.db import models
from .paciente import Paciente
from .profissional import ProfissionalSaude

class Consulta(models.Model):
    data = models.DateTimeField()
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    profissional = models.ForeignKey(ProfissionalSaude, on_delete=models.CASCADE)
