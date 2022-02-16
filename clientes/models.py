from django.db import models

class Clientes(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=20)
    
    def __str__(self):
        return self.nome
