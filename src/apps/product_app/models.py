# This file is used to make the models fot the DB

from django.db import models

# -----------------------------------------------------------------------------


class Categoria(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=100
    )

    def __str__(self):
        return self.nombre


# -----------------------------------------------------------------------------


class Producto(models.Model):
    id = models.AutoField(
        primary_key=True
    )
    nombre = models.CharField(
        max_length=150
    )
    costo = models.DecimalField(
        max_digits=10, decimal_places=2
    )
    descripcion = models.TextField()
    imagen = models.ImageField(
        upload_to="productos/"
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        related_name="productos"
    )

    def __str__(self):
        return self.nombre
