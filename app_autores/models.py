from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    bibliografia = models.TextField(blank=True, null=True) # Puede ser opcional
    pagina_web = models.URLField(max_length=255, blank=True, null=True) # Puede ser opcional

    def __str__(self):
        return f"{self.nombre} {self.apellido}"