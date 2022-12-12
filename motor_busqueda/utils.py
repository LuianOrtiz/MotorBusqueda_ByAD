from motor_busqueda.models import Indice
from bs4 import BeautifulSoup
from urllib.request import urlopen

# https://startupeable.com/directorio/venture-capital/view-accelerator/

def get_enlaces(enlace):
    print(f'Enlace: {enlace}')
    url = urlopen(enlace)
    print('Extraccion de los enlaces de la pag Web')
    bs = BeautifulSoup(url.read(), 'html.parser')
    enlaces_encontrados = []
    contador = 0 
    relacionadas = bs.findAll("div", attrs={"class", "row section-body grid"})
    enlaces_relacionadas = relacionadas[0].find_all("a")
    for enlace in enlaces_relacionadas:
        enlaces_encontrados.append(enlace.get("href")) 
        contador +=1
    print(f'Startups similares encontradas: {contador}')
    print(enlaces_encontrados)
    return enlaces_encontrados

def get_tittle(enlace):
    html = urlopen(enlace)
    bs = BeautifulSoup(html.read(), 'html.parser')
    titulo = str(bs.title.text)
    return titulo

def get_startup_name(enlace):
    html = urlopen(enlace)
    bs = BeautifulSoup(html.read(), 'html.parser')
    h1 = str(bs.h1.text)
    return h1

def get_descripcion(enlace):
    html = urlopen(enlace)
    bs = BeautifulSoup(html.read(), 'html.parser')
    div = bs.findAll("div", attrs={"class","pf-body"})
    descripcion = div[0].find("p").text
    return descripcion

def almacenar_enlaces(enlaces_encontrados):
    for enlace in enlaces_encontrados:
        analisis = Indice(url=enlace, analizado=False, palabra_1="", palabra_2="",palabra_3="")
        analisis.save()
    return 0

def marcar_enlace_revisado(enlace_a_marcar):
    print(f'Enlace a marcar: {enlace_a_marcar}, tipo: {type(enlace_a_marcar)}')
    enlace_update = Indice.objects.filter(url__contains=enlace_a_marcar).first()
    enlace_update.analizado=True
    enlace_update.palabra_1 = get_tittle(enlace_a_marcar)
    enlace_update.palabra_2 = get_startup_name(enlace_a_marcar)
    enlace_update.palabra_3 = get_descripcion(enlace_a_marcar)
    
    enlace_update.save()
    return 0
