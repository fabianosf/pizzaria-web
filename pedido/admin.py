from django.contrib import admin
from .models import Pedido

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('dia_pedido', 'tempo_pedido','nome_pedido','preco_pedido','criado','atualizado')
    
    
