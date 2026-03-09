# django imports
from django.urls import path
# Views
from . import views


urlpatterns = [
    path('select/', views.index),
]
