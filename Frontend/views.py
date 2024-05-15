from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.models import User
from django.contrib import messages, auth
# Create your views here.
from Usuarios.models import UserProfile
from Proyectos.models import Proyecto
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
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'inicio.html', {'proyectos': proyectos, 'user_profile': user_profile})
def Prueba (request):
    return render(request, 'Prueba.html')
