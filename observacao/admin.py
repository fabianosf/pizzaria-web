from django.contrib import admin
from .models import Observacao


@admin.register(Observacao)
class ObservacaoAdmin(admin.ModelAdmin):
    list_display = ('detalhe',)
