from django.shortcuts import redirect, render, get_object_or_404
from . import views
from .models import Categoria, Producto
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import FormProducto, FormAgregarProducto
from django.views.decorators.http import require_POST
from .cart import  Cart
from django.db.models import Q

# Create your views here.
def index(request):
    
    return render(request, "market/index.html", {
        "ultimos" : Producto.objects.all().order_by("-id")[0:3],
        "siguiente" : Producto.objects.all().order_by("-id")[3:10],
        
    })



def producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    form_agregar_producto = FormAgregarProducto()
    return render(request, "market/producto.html", {
        "producto" : un_producto,
        "form_agregar_producto": form_agregar_producto
    })


def acerca_de(request):
    return render(request, "market/acerca_de.html")


def lista_categorias(request):
    lista_categorias = Categoria.objects.all()
    return render(request, "market/layout.html", {
        "lista_categorias":lista_categorias
    })


'''def filtro_secciones(request, seccion_id):
    una_seccion = get_object_or_404(Categoria, id=seccion_id)
    queryset = Articulo.objects.all()
    queryset = queryset.filter(categoria=una_seccion)
    return render(request,"market/index.html", {
        "lista_articulos": queryset,
        "lista_secciones": Categoria.objects.all(),
        "seccion_seleccionada": una_seccion
    })'''


def producto_alta(request):
    if request.method == "POST":
        form = FormProducto(request.POST, request.FILES, instance=Producto(imagen=request.FILES['imagen']))
        if form.is_valid():

            form.save()
        return redirect("market:index")          
    else:
        form = FormProducto()
        return render(request, "market/producto_alta.html", {
            "form": form
        })




def resultado_busqueda(request):

    return render(request, "market/resultado_busqueda.html")

def buscar(request):

    if request.GET["criterio"]:
        
        criterio = request.GET["criterio"]
        productos = Producto.objects.filter(Q(titulo__icontains=criterio) | Q(descripcion__icontains=criterio)).distinct()

        return render(request, "market/resultado_busqueda.html", {
            "query" : criterio,
            "productos" : productos
        } )

    else:
        criterio = request.GET["criterio"]
        productos = []
        return render(request, "market/resultado_busqueda.html", {
            "query" : criterio,
            "productos" : productos
        } )


def buscar_categoria(request, criterio_id):

    una_categoria = get_object_or_404(Categoria, id=criterio_id)

    criterio = una_categoria.categoria
    
    productos = Producto.objects.filter(categoria=criterio_id)

    return render(request, "market/resultado_busqueda.html", {
        "query" : criterio,
        "productos" : productos
    } )

    


def producto_edicion(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    if request.method == "POST":  
        form = FormProducto(data=request.POST, files=request.FILES, instance=un_producto)
        if form.is_valid():
            form.save()
            return redirect("market:index")
    else:
        form = FormProducto(instance = un_producto)
        return render(request, 'market/producto_edicion.html', {
            "producto": un_producto,
            "form": form
        })
    
   
def producto_eliminar(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    un_producto.delete()
    return redirect("market:index")


def finalizar_compra(request):
    pass




'''@login_required
def agregar_producto(request, producto_id):
    un_producto = get_object_or_404(Producto, id=producto_id)
    for id in request.session["agregar_producto"]:
        if id == producto_id:
            #existe el articulo
            return HttpResponseRedirect(reverse("market:producto", args=(un_producto.id,)))            
    request.session["agregar_producto"] += [producto_id]
    return HttpResponseRedirect(reverse("market:producto", args=(un_producto.id,)))  

def ver_carrito(request):
    return render()'''

@require_POST
def cart_add(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    form = FormAgregarProducto(request.POST)
    if form.is_valid:
        #cd = form.cleaned_data
        cart.add(producto = producto, cantidad = form['cantidad'])
    return redirect(reverse('market:index'))

def remover_producto(request, producto_id):
    cart = Cart(request)
    producto = get_object_or_404(Producto, id=producto_id)
    cart.remove(producto)
    return redirect('market:index')

def carrito_compras(request):
    cart = Cart(request)
    return render(request, 'market/carrito.html', {'cart' : cart})

def vaciar_carrito(request):
    cart = Cart(request)
    cart.vaciar_carrito()
    return redirect('market:carrito_compras')