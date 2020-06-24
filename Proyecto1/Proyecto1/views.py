from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader

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

    #nombre = "Hugo"

    #apellido = "Rocha"

    temasDelCurso = ["Plantillas", "Modelos",
                     "Formularios", "Vistas", "Despliegue"]

    ahora = datetime.datetime.now()

    # Aqui Cargamos la plantilla
    open_planitlla = loader.get_template('miplantilla.html')


    # Para darle formato a las cosas simplemnte se crea una variable en el cual abrimos el Template
    #doc_externos = open(
      #  "C:/Users/chama/Desktop/Course_Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    # Leo el Template
    #plt = Template(doc_externos.read())

    # Cierro Template
    #doc_externos.close()

    # Contexto es el argumento para el render, en el cual podemos guardar diccionarios para poder usar estructuras o variables
    # En el argumento del contexto pasamos las variables al igual se puede dar el valor en el mismo contexto
 
    # Renderisamos y lo que pasamos de contexto seria el dicceonario
    documento = open_planitlla.render({"nombre_persona": p1.nombre,
                   "apellido_persona": p1.apellido,
                   "summoner": p1.sumonner,
                   "fecha": ahora,
                   "temas": temasDelCurso})

    return HttpResponse(documento)


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
