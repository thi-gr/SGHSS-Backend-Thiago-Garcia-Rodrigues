from django.db import models
from .administrador import Administrador

class Leito(models.Model):
    numero = models.CharField(max_length=10)
    ocupado = models.BooleanField(default=False)
    administrador = models.ForeignKey(Administrador, on_delete=models.SET_NULL, null=True)
