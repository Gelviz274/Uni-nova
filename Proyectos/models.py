from django.db import models
from Usuarios.models import UserProfile
import os


def upload_to_proyecto_media(instance, filename):
    """Función para definir la ruta de carga de archivos multimedia de proyectos."""
    return os.path.join('Frontend', 'Media', 'videos', 'Videos_proyectos', filename)

def upload_to_actualizacion_media(instance, filename):
    """Función para definir la ruta de carga de archivos multimedia de actualizaciones."""
    return os.path.join('Frontend', 'Media', 'videos', 'Videos_actualizacion', filename)

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    creador = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='proyectos_creados')
    colaboradores = models.ManyToManyField(UserProfile, related_name='proyectos_colaborados')
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    documentacion = models.FileField(upload_to=upload_to_proyecto_media, null=True, blank=True)
    videos = models.FileField(upload_to=upload_to_proyecto_media, null=True, blank=True)
    imagenes = models.ImageField(upload_to=upload_to_proyecto_media, null=True, blank=True)

    def __str__(self):
        return self.nombre_proyecto

class ActualizacionProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    videos = models.FileField(upload_to=upload_to_actualizacion_media, null=True, blank=True)
    imagenes = models.ImageField(upload_to=upload_to_actualizacion_media, null=True, blank=True)

    def __str__(self):
        return f'Actualización de {self.proyecto.nombre} - {self.fecha}'
