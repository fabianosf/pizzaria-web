from django.db import models


class Motoboy(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    
    
    def __str__(self):
        return self.nome