from django import forms

# Models
from .models import (
    Producto,
    Categoria,
)


# -----------------------------------------------------------------------------
# Creacion de un producto nuevo


class AddProduct(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

# -----------------------------------------------------------------------------
# Agregar una nueva categoria


class NewCategory(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
