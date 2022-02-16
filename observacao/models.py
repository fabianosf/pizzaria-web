from django.db import models


class Observacao(models.Model):
    detalhe = models.TextField()
    
    def __str__(self):
        return self.detalhe
