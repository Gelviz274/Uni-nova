from django.urls import path
from .views import iniciar_sesion,registrarse, Inicio, Admin_Inicio, Prueba
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('',Inicio,name='inicio'),
    path('login/',iniciar_sesion,name='iniciar_sesion'),
    path('registrarse/',registrarse,name='registrarse'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('Admin-Inicio',Admin_Inicio,name='inicio_admin'),
    path('Prueba/',Prueba,name='prueba'),
]