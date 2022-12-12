from motor_busqueda.models import Indice


def get_primer_enlace():
    primera_liga = Indice.objects.all()[0:1]
    liga = primera_liga[0]
    return liga

def get_enlaces(enlace):
    from bs4 import BeautifulSoup
    from urllib.request import urlopen
    print(f'Enlace: {enlace}')
    url = urlopen(enlace)
    print('Extraccion de los enlaces de la pag Web')
    bs = BeautifulSoup(url.read(), 'html.parser')
    enlaces_encontrados = []
    contador = 0 
    for enlaces in bs.find_all("a"):
        enlace = format(enlaces.get("href"))
        if enlace[-3:] != "jpg":
            enlaces_encontrados.append("{}".format(enlaces.get("href")))
            print("{}".format(enlaces.get("href")))
            contador = contador + 1
    print("\nEnlaces encontrados: ", contador)
    return enlaces_encontrados

def almacenar_enlaces(enlaces_encontrados):
    for enlace in enlaces_encontrados:
        analisis = Indice(url=enlace, analizado=False, palabra_1="", palabra_2="",palabra_3="")
        analisis.save()
    return 0

def marcar_enlace_revisado(enlace_a_marcar):
    print(f'Enlace a marcar: {enlace_a_marcar}, tipo: {type(enlace_a_marcar)}')
    enlace_update = Indice.objects.filter(url__contains=enlace_a_marcar).first()
    enlace_update.analizado=True
    enlace_update.save()
    return 0
