from django.db import models


class Categoria(models.Model):
    CATEGORIA_CHOICES = (
        ('S', 'PIZZA SALGADA'),
        ('D', 'PIZZA DOCE'),
        ('B', 'BEBIDA'),
        ('O', 'OUTRO')
    )
    status = models.CharField(max_length=2, choices=CATEGORIA_CHOICES)
    
    
    def __str__(self):
        return self.status
