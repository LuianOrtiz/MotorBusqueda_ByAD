from django.shortcuts import render
from motor_busqueda.models import Indice
# Create your views here.

def index(request):

    return render(request, 'index.html')

def url_inicial(request):
    analisis = Indice(url=request.POST['url'], analizado=request.POST['analizado'], palabra_1=request.POST['palabra_1'], palabra_2=request.POST['palabra_2'],palabra_3=request.POST['palabra_3'])
    analisis.save()
    return render(request, 'enlaces.html')
