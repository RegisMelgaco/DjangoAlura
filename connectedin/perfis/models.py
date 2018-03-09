from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length = 50, null=False)
	email = models.CharField(max_length = 50, null=False)
	telefone = models.CharField(max_length = 20, null=False)
	nome_empresa = models.CharField(max_length = 40, null=False)