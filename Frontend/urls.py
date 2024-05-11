from django.urls import path
from .views import  iniciar_sesion,registrarse, Inicio, Admin_Inicio, Prueba, activate, cerrar_sesion
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',Inicio,name='inicio'),
    path('iniciar_sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('Admin-Inicio',Admin_Inicio,name='inicio_admin'),
    path('Prueba/',Prueba,name='prueba'),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('cerrar_sesion/', cerrar_sesion, name='cerrar_sesion'),
]