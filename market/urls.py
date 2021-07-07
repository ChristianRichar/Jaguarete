from django.urls import path
from . import views

app_name = "market"
urlpatterns = [
    path('', views.index, name="index"),
    path('<int:producto_id>', views.producto, name="producto"),
    path('market/acerca_de', views.acerca_de, name="acerca_de"),
    path('lista_categorias', views.lista_categorias, name="lista_categorias"),
    path('producto_alta', views.producto_alta, name="producto_alta"),
    path('producto_edicion/<int:producto_id>', views.producto_edicion, name="producto_edicion"),
    path('producto_eliminar/<int:producto_id>', views.producto_eliminar, name="producto_eliminar"),
    path('resultado_busqueda/', views.resultado_busqueda, name="resultado_busqueda"),
    path('buscar/', views.buscar, name="buscar"),
    path('buscar_categoria/<int:criterio_id>', views.buscar_categoria, name="buscar_categoria"),
    path('carrito_compras/', views.carrito_compras, name="carrito_compras"),
    path('cart_add/<int:producto_id>', views.cart_add, name="cart_add"),
    path('remover_producto/<int:producto_id>', views.remover_producto, name="remover_producto"),
    path('vaciar_carrito/', views.vaciar_carrito, name="vaciar_carrito"),
    #path('agregar_producto/<int:producto_id>', views.agregar_producto, name="agregar_producto"),
    #path('finalizar_compra/<int:carrito_id>', views.finalizar_compra, name="finalizar_compra"),
    #path('vaciar_carrito/<int:carrito_id>', views.vaciar_carrito, name="vaciar_carrito"),
    
    
]