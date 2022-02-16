from django.db import models
from cliente .models import Cliente

class Pagamento(models.Model):
    PAGAMENTO_CHOICES = (
        ('D', 'DINHEIRO'),
        ('C', 'CARTAO'),
        ('P', 'PIX')
    )    
    pagamento = models.CharField(max_length=1, choices=PAGAMENTO_CHOICES)  
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
