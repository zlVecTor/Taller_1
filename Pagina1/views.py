from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def Pagina1Template(request):
    return render(request, 'Pagina1.html')