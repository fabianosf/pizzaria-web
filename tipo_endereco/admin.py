from django.contrib import admin
from .models import TipoEndereco



@admin.register(TipoEndereco)
class TipoEnderecoAdmin(admin.ModelAdmin):
    list_display = ('status',)

