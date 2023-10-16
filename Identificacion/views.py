from django.shortcuts import render

from django.http import HttpResponse

from django.contrib import messages
# Create your views here.

def IdentificacionTemplate(request):
    return render(request, 'Identificacion.html')


from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login

def registro_view(request):
    if request.method == 'POST':
        # Procesa el registro aquí (crea un nuevo usuario, etc.)
        # Luego redirige al usuario a la página de inicio de sesión
        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('inicio-sesion')

    return render(request, 'Identificacion.html')

def inicio_sesion_view(request):
    if request.method == 'POST':
        # Procesa el inicio de sesión aquí (autentica al usuario, etc.)
        # Luego redirige al usuario al menú
        return redirect('menu')

    return render(request, 'Identificacion.html')
