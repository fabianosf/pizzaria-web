from django.db import models
from cliente .models import Cliente

class Pedido(models.Model):
    PEDIDO_CHOICES = (
        ('P', 'PEDIDO_REALIZADO'),
        ('F', 'FAZENDO'),
        ('S', 'SAIU PARA ENTREGA')
    )
    dia_pedido = models.DateField()
    tempo_pedido = models.CharField(max_length=100, null=True, blank=True)
    nome_pedido = models.CharField(max_length=100, null=True, blank=True)
    preco_pedido = models.DecimalField(max_digits=5, decimal_places=2)
    status = models.CharField(max_length=1, choices=PEDIDO_CHOICES)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome_pedido
