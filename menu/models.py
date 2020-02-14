from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre del Plato")    
    description = models.TextField(verbose_name="Descripción")
    price = models.DecimalField(verbose_name="Precio", max_digits=5, decimal_places=2)
    image = models.ImageField(verbose_name="Imagen", upload_to="menus")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creaciòn")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Ediciòn")

    class Meta:
        verbose_name = "menu"
        verbose_name_plural = "menus"
        ordering = ['name']

    def __str__(self):
        return self.name
