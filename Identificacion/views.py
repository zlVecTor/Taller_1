from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def IdentificacionTemplate(request):
    return render(request, 'Identificacion.html')