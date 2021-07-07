from django import forms
from .models import Producto

class FormProducto(forms.ModelForm):

    #campos del modelo
    class Meta:
        model = Producto
        fields = '__all__'


#cantidad_de_productos = [(i, str(i)) for i in range(1,21)]

class FormAgregarProducto(forms.Form):
    cantidad = forms.IntegerField()
    #cantidad = forms.TypedChoiceField(choices=cantidad_de_productos, coerce=int)
    #update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
     
        