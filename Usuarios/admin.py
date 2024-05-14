from django.contrib import admin
from .models import UserProfile, Carrera, Universidad, Semestre

class CarreraAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'universidad_nombre') # Muestra el nombre de la carrera y el nombre de la universidad

    def universidad_nombre(self, obj):
        return obj.universidad.nombre

    universidad_nombre.short_description = 'Universidad' # Cambia el encabezado de la columna en el panel de administrador

admin.site.register(Carrera, CarreraAdmin)

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'username')

    def first_name(self, obj):
        return obj.user.first_name
    
    first_name.short_description = 'Primer Nombre'

    def username(self, obj):
        return obj.user.username
    
    username.short_description = 'Nombre de usuario'

admin.site.register(UserProfile, UserProfileAdmin)

admin.site.register(Universidad)
admin.site.register(Semestre)





