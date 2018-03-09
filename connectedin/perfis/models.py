from django.db import models

class Perfil(models.Model):
	nome = models.CharField(max_length = 50)
	email = models.CharField(max_length = 50)
	telefone = models.CharField(max_length = 20)
	nome_empresa = models.CharField(max_length = 40)