from django.db import models
from django.contrib.auth.models import User
# Modelo de gestion de stock

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Mangas(models.Model):
    nombre = models.CharField(max_length=150)
    tomo = models.IntegerField()
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    demografia = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    imagen = models.ImageField(upload_to='mangas_images/')

    def __str__(self):
        return f"{self.nombre}"
    #podemos crear la clase "Meta" para arreglar errores ortográficos u ordenar en qué orden ver los elementos con "ordering[]"

class Libros(models.Model):
    nombre = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    imagen = models.ImageField(upload_to='libros_images/')
    
    def __str__(self):
        return f"{self.nombre}"
    
class Comics(models.Model):
    nombre = models.CharField(max_length=150)
    editorial = models.CharField(max_length=150)
    autor = models.CharField(max_length=150)
    genero = models.CharField(max_length=150)
    cantidad_stock = models.IntegerField()
    cantidad_hojas = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    imagen = models.ImageField(upload_to='comics_images/')
    
    def __str__(self):
        return f"{self.nombre}"
    
class Figuras(models.Model):
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=10, decimal_places=2) 
    cantidad_stock = models.IntegerField()
    imagen = models.ImageField(upload_to='figuras_images/')

    def __str__(self):
        return f"{self.nombre}"