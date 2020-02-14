from django.db import models

# Create your models here.
class Chef(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombres")
    direccion = models.TextField(max_length=200, verbose_name="Dirección")
    titulo = models.TextField(max_length=200, verbose_name="Titulo")
    image = models.ImageField(verbose_name="Imagen", upload_to="chef", null=True, blank=True)
    facebook = models.URLField(max_length=200, verbose_name="Facebook", null=True, blank=True)
    instagram = models.URLField(max_length=200, verbose_name="Instagram", null=True, blank=True)
    twitter = models.URLField(max_length=200, verbose_name="Twiter", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")  
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Edición")

    class Meta:
        verbose_name = "chef"
        verbose_name_plural = "chefs"
        ordering = ['name']

    def __str__(self):
        return self.name


