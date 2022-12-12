from django.shortcuts import render
from motor_busqueda.models import Indice
from motor_busqueda.utils import get_primer_enlace, get_enlaces, almacenar_enlaces, marcar_enlace_revisado
# Create your views here.

def index(request):
    return render(request, 'index.html')

def url_inicial(request):
    analisis = Indice(url=request.POST['url'], analizado=request.POST['analizado'], palabra_1=request.POST['palabra_1'], palabra_2=request.POST['palabra_2'],palabra_3=request.POST['palabra_3'])
    analisis.save()
    primer_enlace = get_primer_enlace()
    enlaces_encontrados = get_enlaces(str(primer_enlace))
    almacenar_enlaces(enlaces_encontrados)
    marcar_enlace_revisado(str(primer_enlace))
    context = {
        "primer_enlace": primer_enlace,
        "enlaces_encontrados": enlaces_encontrados,
    }
    return render(request, 'enlaces.html', context)

