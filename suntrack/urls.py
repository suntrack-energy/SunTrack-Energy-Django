from django.urls import path
from suntrack.views import index, servico, buscar

urlpatterns = [
    path('', index, name='index'),
    path('servico/<int:imagem_id>', servico, name='servico'),
    path('buscar', buscar, name='buscar'),
]