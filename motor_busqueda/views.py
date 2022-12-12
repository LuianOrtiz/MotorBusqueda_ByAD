from django.shortcuts import render
from motor_busqueda.models import Indice
from motor_busqueda.utils import  get_enlaces, almacenar_enlaces, marcar_enlace_revisado
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inicio(request): 
    return render(request, 'inicio.html')

def url_inicial(request):
    analisis = Indice(url=request.POST['url'], analizado=False, palabra_1='', palabra_2='',palabra_3='')
    analisis.save()
    primer_enlace = request.POST['url']
    enlaces_encontrados = get_enlaces(str(primer_enlace))
    almacenar_enlaces(enlaces_encontrados)
    marcar_enlace_revisado(str(primer_enlace))
    context = {
        "primer_enlace": primer_enlace,
        "enlaces_encontrados": enlaces_encontrados,
    }
    return render(request, 'enlaces.html', context)

def busqueda_enlaces(request):
    sin_analizar = Indice.objects.filter(analizado=False)
    for enlace in sin_analizar:
        marcar_enlace_revisado(str(enlace))
    
    startups = Indice.objects.all()
    context = {
        "startups": startups,
    }
    return render(request, 'startups.html', context)

def startups(request): 
    startups = Indice.objects.all()
    context = {
        "startups": startups,
    }
    return render(request, 'startups.html', context)
    
