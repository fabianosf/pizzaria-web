from django.db import models


class Produto(models.Model):   
    nome_produto = models.CharField(max_length=100, null=False, blank=False)    
    preco_produto = models.DecimalField(max_digits=5, decimal_places=2)
    ingrediente_produto = models.CharField(max_length=100, null=False, blank=False)
    
    def __str__(self):
        return self.nome_produto