from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.
from Usuarios.models import UserProfile
from Proyectos.models import Proyecto
from django.urls import reverse
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.contrib.auth.decorators import login_required

# VISTA LOGIN.HTML
def iniciar_sesion(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('inicio_admin') #Dashboard de Admin 
                else:
                    return redirect('inicio')  #Pagina Principal
            else:
                messages.error(request, 'Nombre de usuario o contraseña incorrectos.')

        return render(request, 'login.html')




def registrarse(request):
    if request.user.is_authenticated:
        return redirect('inicio')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']

            if User.objects.filter(username=username).exists():
                messages.error(request, 'El nombre de usuario ya está en uso.')
                return redirect('registrarse')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'El correo electrónico ya está en uso.')
                return redirect('registrarse')
            else:
                try:
                    nuevo_usuario = User.objects.create_user(username=username, email=email, password=password)
                    nuevo_usuario.is_active = False
                    nuevo_usuario.save()

                    # Activación de usuario
                    current_site = get_current_site(request)
                    mail_subject = '¡ Activa tu cuenta en Uninova !'
                    message = render_to_string('account_verification_email.html', {
                        'user': nuevo_usuario,
                        'domain': current_site.domain,
                        'uid': urlsafe_base64_encode(force_bytes(nuevo_usuario.pk)),
                        'token': default_token_generator.make_token(nuevo_usuario),
                    })
                    to_email = email
                    send_email = EmailMessage(mail_subject, message, to=[to_email])
                    send_email.send()
                    
                    messages.success(request, 'Se ha enviado un correo electrónico de activación. Por favor, verifica tu cuenta.')
                    return redirect('iniciar_sesion')
                except IntegrityError:
                    messages.error(request, 'El correo electrónico ya está en uso.')
                    return redirect('registrarse')
                except Exception as e:
                    messages.error(request, 'Hubo un error al verificar tu cuenta. Por favor, inténtalo de nuevo.')
                    return redirect('registrarse')
        return render(request, 'registrarse.html')    # Renderizar el formulario de registro

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, '¡Tu cuenta ha sido activada exitosamente! Por favor, inicia sesión.')
        return redirect('iniciar_sesion')
    else:
        messages.error(request, 'El enlace de activación es inválido o ha expirado.')
        return redirect('iniciar_sesion')
@login_required
def cerrar_sesion(request):
    auth.logout(request)
    return redirect('iniciar_sesion')    





def Admin_Inicio (request):
    return render(request, 'inicio_admin.html')


@login_required(login_url='iniciar_sesion')
def Inicio(request):
    # Obtener todos los proyectos de la base de datos
    proyectos = Proyecto.objects.all()
    
    # Obtener el perfil del usuario actual
    user_profile = get_object_or_404(UserProfile, user=request.user)

    # Lista para almacenar los perfiles de los creadores de proyectos
    perfiles_creadores = []

    # Obtener los perfiles de los creadores de proyectos
    for proyecto in proyectos:
        try:
            perfil_creador = UserProfile.objects.get(user=proyecto.creador)
            perfiles_creadores.append(perfil_creador)
        except UserProfile.DoesNotExist:
            # Si el perfil de usuario no existe para el creador de este proyecto, agregar None a la lista
            perfiles_creadores.append(None)
    
    return render(request, 'inicio.html', {'proyectos': proyectos, 'user_profile': user_profile, 'perfiles_creadores': perfiles_creadores})
@login_required(login_url='iniciar_sesion')
def Prueba(request):
    # Obtener todos los proyectos de la base de datos
    proyectos = Proyecto.objects.all()
    # Obtener el perfil del usuario actual
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'Menu.html', {'proyectos': proyectos, 'user_profile': user_profile})
"""def Prueba (request):
    return render(request, 'Prueba.html')"""


@login_required
def perfil_usuario(request, username): 
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(UserProfile, user=user)
    proyectos_creados = Proyecto.objects.filter(creador=user)
    proyectos_colaborados = user.proyectos_colaborados.all()
    universidad_usuario = user_profile.universidad
    
    return render(request, 'perfil_user.html', {
        'user': user,
        'universidad_usuario': universidad_usuario,
        'proyectos_creados': proyectos_creados,
        'proyectos_colaborados': proyectos_colaborados,
        'user_profile': user_profile
    })



@login_required
def edit_user(request):
    if request.method == 'POST':
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellido')
        user.save()
        
        # Genera la nueva URL del perfil
        perfil_url = reverse('ver_perfil', kwargs={'username': user.username})
        
        # Devuelve la nueva URL en la respuesta JSON
        return JsonResponse({'success': True, 'message': 'Cambios guardados exitosamente.', 'url': perfil_url})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)
    

def crear_proyecto(request):
    if request.method == 'POST':
        # Obtener los datos del formulario del request
        nombre_proyecto = request.POST.get('nombre_proyecto')
        descripcion = request.POST.get('descripcion')
        documentacion = request.FILES.get('documentacion')
        videos = request.FILES.get('videos')
        imagenes = request.FILES.get('imagenes')

        # Crear el nuevo proyecto en la base de datos
        proyecto = Proyecto.objects.create(
            nombre_proyecto=nombre_proyecto,
            creador=request.user,
            descripcion=descripcion,
            documentacion=documentacion,
            videos=videos,
            imagenes=imagenes
        )

        # Redirigir a la página del proyecto creado
        return redirect('ver_proyecto', proyecto_id=proyecto.id)
    
    return render(request, 'inicio.html')

def ver_proyecto(request, proyecto_id):
    proyecto = get_object_or_404(Proyecto, id=proyecto_id)
    return render(request, 'ver_proyecto.html', {'proyecto': proyecto})

def Prueba (request):
    return render(request, 'Prueba.html')