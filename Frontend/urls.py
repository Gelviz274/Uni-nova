from django.urls import path
from .views import *#iniciar_sesion,registrarse, Inicio, Admin_Inicio, Prueba, activate, cerrar_sesion, edit_user, perfil_usuario
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('crear_proyecto/', crear_proyecto, name='crear_proyecto'),
    path('proyecto/<int:proyecto_id>/', ver_proyecto, name='ver_proyecto'),
    path('crear_proyecto/',crear_proyecto,name='crear_proyecto'),
    path('inicio/',Inicio,name='inicio'),
    path('<username>/', perfil_usuario, name='ver_perfil'),
    path('', RedirectView.as_view(url='/inicio/', permanent=True)),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('edit_user/', edit_user, name='edit_user'),
    path('Admin-Inicio',Admin_Inicio,name='inicio_admin'),
    path('Prueba/',Prueba,name='prueba'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)