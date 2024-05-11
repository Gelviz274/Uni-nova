from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.contrib.auth.models import BaseUserManager
import os

def upload_to_usuario_media(instance, filename):
    """Función para definir la ruta de carga de las fotos de perfil de usuario."""
    return os.path.join('Frontend', 'Media', 'imagenes', 'fotos_usuarios', filename)


class Universidad(models.Model):
    nombre = models.CharField(max_length=255)
    
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=255)
    universidad = models.ForeignKey(Universidad, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre

class Semestre(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class UserProfile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    semestre = models.ForeignKey(Semestre, on_delete=models.SET_NULL, null=True, blank=True)
    universidad = models.ForeignKey(Universidad, on_delete=models.SET_NULL, null=True, blank=True)
    carrera = models.ForeignKey(Carrera, on_delete=models.SET_NULL, null=True, blank=True)
    foto_perfil = models.ImageField(upload_to=upload_to_usuario_media, null=True, blank=True)
    acerca_de_mi = models.TextField(null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    groups = models.ManyToManyField('auth.Group')
    user_permissions = models.ManyToManyField('auth.Permission')
    def __str__(self):
        return self.user.first_name
    







class UserManager(BaseUserManager):

    def create_user(self, username, email, password=None):
        """
        Crea y guarda un usuario con el correo electrónico y la contraseña dados.
        """
        if not email:
            raise ValueError('El usuario debe tener un correo electrónico')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None):
        """
        Crea y guarda un superusuario con el correo electrónico y la contraseña dados.
        """
        user = self.create_user(username, email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user



