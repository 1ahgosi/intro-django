from django.shortcuts import render, get_object_or_404
from .models import Artigo, Categoria, Vendedor

def lista_artigos(request):
    """Vista de artigos disponíveis."""
    artigos = Artigo.objects.all().order_by('-data_de_criacao')
    # Alterado de 'core/lista_artigos.html' para 'loja/lista_artigos.html'
    return render(request, 'loja/lista_artigos.html', {'artigos': artigos})

def artigos_por_categoria(request, categoria_id):
    """Vista de artigos de cada categoria individual."""
    categoria = get_object_or_404(Categoria, id=categoria_id)
    artigos = categoria.artigos.all() 
    # Alterado de 'core/artigos_por_categoria.html' para 'loja/artigos_por_categoria.html'
    return render(request, 'loja/artigos_por_categoria.html', {'categoria': categoria, 'artigos': artigos})

def perfil_vendedor(request, vendedor_id):
    """Perfil do vendedor."""
    vendedor = get_object_or_404(Vendedor, id=vendedor_id)
    artigos = vendedor.artigos.all()
    # Alterado de 'core/perfil_vendedor.html' para 'loja/perfil_vendedor.html'
    return render(request, 'loja/perfil_vendedor.html', {'vendedor': vendedor, 'artigos': artigos})