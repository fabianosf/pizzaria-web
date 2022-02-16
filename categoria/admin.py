from django.contrib import admin
from .models import Categoria



@admin.register(Categoria)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('status',)
