from django.db import models
from .consulta import Consulta

class Receita(models.Model):
    descricao = models.TextField()
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
