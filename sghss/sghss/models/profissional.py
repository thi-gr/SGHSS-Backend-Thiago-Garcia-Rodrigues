from django.db import models
from django.contrib.auth.models import User

class ProfissionalSaude(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    especialidade = models.CharField(max_length=100)
