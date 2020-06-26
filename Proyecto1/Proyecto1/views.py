from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

# Se crea una clase en la cual es una Persona con sus parametros


class Persona(object):
    # Inicializamos su constructor init lleva dos guiones
    def __init__(self, nombre, apellido, sumonner):

        self.nombre = nombre

        self.apellido = apellido

        self.sumonner = sumonner

# primera vista


def saludo(request):

    # Aqui pasamos los parametros de una persona
    p1 = Persona("Javier", "Aguayo", "El Sombreroo")


    temasDelCurso = ["Plantillas", "Modelos",
                     "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    # Aqui Cargamos la plantilla
    open_planitlla = loader.get_template('miplantilla.html')


    return render(request, "miplantilla.html", {"nombre_persona": p1.nombre,
                   "apellido_persona": p1.apellido,
                   "summoner": p1.sumonner,
                   "fecha": ahora,
                   "temas": temasDelCurso})


def despedida(request):
    return HttpResponse("Gracias por visitar esta pagina")

# Esto regresa la fecha actual


def dameFecha(reequest):
    fecha_actal = datetime.datetime.now()

    documento = """
    <div>
    <body>
    <h1>
        Fecha y hora actuales %s
    </h1>
    <body>
    </div>""" % fecha_actal

    return HttpResponse(documento)


def calculaEdad(request, agno, edad):

    periodo = agno - 2020
    edadFutura = edad + periodo
    documento = """
    
    <div>
    <body>
    <h2>
    En el año %s tendras %s años
    </h2>
    </bodo>
    </div>
    """ % (agno, edadFutura)

    return HttpResponse(documento)

def cursoC(request):
    fecha_actal = datetime.datetime.now()

    return render(request, "CursoC.html", {"dameFecha": fecha_actal})

def cursoCss(request):
    fecha_actal = datetime.datetime.now()

    return render(request, "cursoCss.html", {"dameFecha": fecha_actal})
