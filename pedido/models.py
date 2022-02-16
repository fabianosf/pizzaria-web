from django.db import models


class Pedido(models.Model):
    dia_pedido = models.DateField()
    tempo_pedido = models.CharField(max_length=100, null=True, blank=True)
    nome_pedido = models.CharField(max_length=100, null=True, blank=True)
    preco_pedido = models.DecimalField(max_digits=5, decimal_places=2)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_pedido
