
from django.conf import settings
from .models import Producto

class Cart(object):
    def __init__(self, request):
        '''Inicializa carrito'''
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, producto, cantidad, update_quantity=False):
        producto_id = str(producto.id)
        if producto_id not in self.cart:
            self.cart[producto_id] = {'cantidad' : str(cantidad), 'precio' : str(producto.precio)}
        '''if update_quantity:
            self.cart[producto_id]['cantidad'] = cantidad
        else:
            self.cart[producto_id]['cantidad'] += cantidad'''
        self.save()

    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart

        self.session.modified = True

    def remove(self, producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def __iter__(self):
        productos_id = self.cart.keys()
        productos = Producto.objects.filter(id__in=productos_id)

        '''for producto in porductos:
            self.cart[str(producto.id)] = producto'''

        for item in productos:
            
            yield item

        

    def cant_productos(self):
        return sum( item['cantidad'] for item in self.cart.values())

    def total_carrito(self):
        suma = 0
        for item in self.cart.values():
            precio = int(item['precio'])
            cantidad = item['cantidad']
            suma += precio

        return suma

    def vaciar_carrito(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True 

    

