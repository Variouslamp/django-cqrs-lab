# django imports
from django.urls import path
# Views
from .views import (
    add_product,
    new_category,
)


urlpatterns = [
    path('add/', add_product),
    path('add-category/', new_category,),
]
