from django.db import models

# Create your models here.

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)
    Localidad = models.CharField(max_length=100)
    email = models.EmailField()
    cedes = models.PositiveIntegerField()

    def __str__(self):
        return self.nombre

class Libro(models.Model):
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    costo = models.PositiveIntegerField()
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.titulo