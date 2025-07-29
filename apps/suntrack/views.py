from django.shortcuts import render, get_object_or_404
from apps.suntrack.models import Servicos

def index(request):
    servicos = Servicos.objects.filter(publicada=True)

    return render(request, 'suntrack-energy/index.html', {'cards': servicos})

def servico(request, imagem_id):
    servicos = get_object_or_404(Servicos, pk=imagem_id) # pk -> Primary Key
    return render(request, 'suntrack-energy/servico.html', {'servicos': servicos})

def buscar(request):
    servicos = Servicos.objects.filter(publicada=True)

    if 'buscar' in request.GET:
        titulo_a_buscar = request.GET['buscar']
        if titulo_a_buscar:
            servicos = servicos.filter(titulo__icontains=titulo_a_buscar)

    return render(request, 'suntrack-energy/buscar.html', {'cards': servicos})