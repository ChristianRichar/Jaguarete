from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    categoria = models.CharField(max_length=64, null=False)

    def __str__(self):
        return f"{self.categoria}"

class Producto(models.Model):
    titulo = models.CharField(max_length=128, null=False)
    imagen = models.FileField(upload_to='imagenes/', null=False)
    descripcion = models.CharField(max_length = 2000, null=False)
    precio = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name="categoria_producto")

    def __str__(self): 
        return f"{self.titulo}: {self.descripcion}"

'''class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    productos = models.ManyToManyField(Producto)
    #precio_total = precio_tot()

    def agregar_producto(self, producto_nuevo):
        productos.add(producto_nuevo)
    
    def quitar_producto(self, prododucto_eliminar):
        producto_nuevo.remove(producto_eliminar)

    def vaciar_carrito(self):
        productos.clear()

    def precio_tot(self):
        precio_total = productos.object.precio.sum()
        return precio_total
    
    def __str__(self):
        return f"{usuario}: {productos}. precio total = {precio_total}"'''