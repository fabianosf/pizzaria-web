from django.db import models


class Endereco(models.Model):
    COMPLEMENTO_CHOICES = (
        ('C', 'CASA'),
        ('A', 'APARTAMENTO'),
    )
    endereco = models.CharField(max_length=100, null=False, blank=False)
    numero = models.CharField(max_length=4, null=False, blank=False)  
    complemento_choices = models.CharField(max_length=1, choices=COMPLEMENTO_CHOICES)    
    cidade = models.CharField(max_length=50, null=False, blank=False)
    bairro = models.CharField(max_length=50, null=False, blank=False)
    
    
    def __str__(self):
        return self.endereco
    
    
    