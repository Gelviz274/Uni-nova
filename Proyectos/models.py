from django.db import models
from Usuarios.models import UserProfile
from django.contrib.auth.models import User
import os


def upload_to_proyecto_media(instance, filename):
    """Función para definir la ruta de carga de archivos multimedia de proyectos."""
    return os.path.join('documentos', 'doc_proyectos', filename)
#SUBIR VIDEOS
def upload_to_actualizacion_media(instance, filename):
    """Función para definir la ruta de carga de archivos multimedia de actualizaciones."""
    return os.path.join('videos', 'Videos_actualizacion', filename)

class Proyecto(models.Model):
    nombre_proyecto = models.CharField(max_length=255)
    creador = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos_creados')
    colaboradores = models.ManyToManyField(User, through='ProyectoColaborador', related_name='proyectos_colaborados')
    fecha_creacion = models.DateField(auto_now_add=True)
    descripcion = models.TextField()
    documentacion = models.FileField(upload_to=upload_to_proyecto_media, null=True, blank=True)
    
    

    def __str__(self):
        return self.nombre_proyecto

class ProyectoImagen(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to='proyecto_imagenes')

    def __str__(self):
        return f'Imagen de {self.proyecto.nombre_proyecto}'

class ProyectoVideo(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to=upload_to_proyecto_media)

    def __str__(self):
        return f'Video de {self.proyecto.nombre_proyecto}'




class ActualizacionProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return f'Actualización de {self.proyecto.nombre} - {self.fecha}'


class ActualizacionProyectoImagen(models.Model):
    actualizacion = models.ForeignKey(ActualizacionProyecto, on_delete=models.CASCADE, related_name='imagenes')
    imagen = models.ImageField(upload_to=upload_to_actualizacion_media)

    def __str__(self):
        return f'Imagen de la actualización de {self.actualizacion.proyecto.nombre_proyecto} - {self.actualizacion.fecha}'

class ActualizacionProyectoVideo(models.Model):
    actualizacion = models.ForeignKey(ActualizacionProyecto, on_delete=models.CASCADE, related_name='videos')
    video = models.FileField(upload_to=upload_to_actualizacion_media)

    def __str__(self):
        return f'Video de la actualización de {self.actualizacion.proyecto.nombre_proyecto} - {self.actualizacion.fecha}'


class ProyectoColaborador(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.usuario.username} colabora en {self.proyecto.nombre_proyecto}'