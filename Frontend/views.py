from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
# Create your views here.
from Usuarios.models import UserN
from Proyectos.models import Proyecto
from django.contrib import messages

def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('inicio_admin')  # Redirige al panel de administrador
            else:
                return redirect('inicio')  # Redirige a la página de inicio
        else:
            messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

    return render(request, 'login.html')
def Admin_Inicio (request):
    return render(request, 'inicio_admin.html')

def Inicio (request):
    return render(request, 'inicio.html')

def Prueba (request):
    return render(request, 'Prueba.html')


"""
def iniciar_sesion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Iniciar sesión
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            # Usuario autenticado correctamente, redirigir a la página de inicio o donde sea necesario
            return redirect('iniciopagina')
        else:
            # Usuario no autenticado, mostrar mensaje de error
            return JsonResponse({'error': 'Usuario o contraseña incorrectos'})

    return render(request, 'login.html')
"""

def registrarse(request):
    if request.method == 'POST':
        # Procesar los datos del formulario
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return JsonResponse({'mensaje': 'El nombre de usuario ya está en uso.'})
        elif User.objects.filter(email=email).exists():
            return JsonResponse({'mensaje': 'El correo electrónico ya está en uso.'})
        else:
            try:
                
                nuevo_usuario = UserN.objects.create_user(username=username, email=email, password=password)
                return JsonResponse({'mensaje': 'Usuario creado exitosamente.'})
            except IntegrityError:
                return JsonResponse({'mensaje': 'El correo electrónico ya está en uso.'})

    return JsonResponse({'mensaje': 'Error: método no permitido.'}, status=405)

