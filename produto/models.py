from django.db import models
from categoria .models import Categoria


class Produto(models.Model):   
    nome_produto = models.CharField(max_length=100, null=False, blank=False)    
    preco_produto = models.DecimalField(max_digits=5, decimal_places=2)
    ingrediente_produto = models.CharField(max_length=100, null=False, blank=False)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nome_produto