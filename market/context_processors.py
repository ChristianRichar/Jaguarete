from .models import Categoria

def list_categorias(request):

    lista_categorias = Categoria.objects.all()
    return {
        'categorias': lista_categorias
    }