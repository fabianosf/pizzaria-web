from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    telefone = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=100)
    usuario = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=20)
     
    
    def __str__(self):
        return self.nome
