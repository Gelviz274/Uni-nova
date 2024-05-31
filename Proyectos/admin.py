from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Proyecto)
admin.site.register(ProyectoColaborador)
admin.site.register(ProyectoImagen)
admin.site.register(ProyectoVideo)
admin.site.register(ActualizacionProyectoImagen)
admin.site.register(ActualizacionProyectoVideo)
