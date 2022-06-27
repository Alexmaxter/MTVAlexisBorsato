

from datetime import datetime
from django.http import HttpResponse


def inicio(request):
    return HttpResponse("Mi primer vista")

def ver_fecha(request):

    fecha = datetime.now()

    return HttpResponse(f"Fecha: {fecha}")

def saludo(request, nombre):

    return HttpResponse(f"Hola {nombre}")

def mi_template(request):

    return HttpResponse(f"Pagina web")