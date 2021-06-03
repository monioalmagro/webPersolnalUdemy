from django.db import models
from django.db.models.fields import DateTimeField


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripción")
    image = models.ImageField(verbose_name="Imagen",upload_to="projects")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Actualización")
    
    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
        ordering = ['-created']

    def __str__(self) -> str:
        return self.title
