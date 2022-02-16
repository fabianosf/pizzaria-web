from django.db import models


class Categoria(models.Model):
    CATEGORIA_CHOICES = (
        ('PIZZA SALGADA', 'PIZZA SALGADA'),
        ('PIZZA DOCE', 'PIZZA DOCE'),
        ('BEBIDA', 'BEBIDA'),
        ('OUTRO', 'OUTRO')
    )
    categoria = models.CharField(max_length=15, choices=CATEGORIA_CHOICES)
    
    
    def __str__(self):
        return self.categoria
    
    
