from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def Pagina2Template(request):
    return render(request, 'Pagina2.html')