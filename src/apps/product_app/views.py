# Django
from django.shortcuts import (
    render,
    redirect
)

# Forms
from .forms import (
    AddProduct,
    NewCategory
)

# -----------------------------------------------------------------------------


def add_product(request):
    if request.method == "POST":
        form = AddProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/thanks/")
    else:
        form = AddProduct()
    return render(request, "product_app/crear_producto.html", {"form": form})

# -----------------------------------------------------------------------------


def new_category(request):
    if request.method == 'POST':
        form = NewCategory(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/product/add/")
    else:
        form = NewCategory()
    return render(
        request,
        "product_app/crear_categoria.html",
        {"form": form}
        )
