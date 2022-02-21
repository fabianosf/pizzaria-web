from django.urls import path
from .views import home

urlpatterns = [
    path('', home), # principal da pagina    
]
