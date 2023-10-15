from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def Pagina3Template(request):
    return render(request, 'Pagina3.html')