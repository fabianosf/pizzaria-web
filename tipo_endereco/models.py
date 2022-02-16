from django.db import models
from endereco .models import Endereco

class TipoEndereco(models.Model):
    TIPO_ENDERECO_CHOICES = (
        ('S', 'CASA'),
        ('D', 'TRABALHO'),        
        ('O', 'OUTRO')
    )
    status = models.CharField(max_length=2, choices=TIPO_ENDERECO_CHOICES)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE)
    
