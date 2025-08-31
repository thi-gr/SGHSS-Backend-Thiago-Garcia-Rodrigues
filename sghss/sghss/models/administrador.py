from django.db import models

class Administrador(models.Model):
    nome = models.CharField(max_length=100)
