from django.db import models


class Pagamento(models.Model):
    PAGAMENTO_CHOICES = (
        ('D', 'DINHEIRO'),
        ('C', 'CARTAO'),
        ('P', 'PIX')
    )    
    pagamento = models.CharField(max_length=1, choices=PAGAMENTO_CHOICES)  
    
