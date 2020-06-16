from django.http import HttpResponse
import datetime
from django.template import Template, Context


class Persona(object):
    def __init__(self, nombre, apellido):

        self.nombre = nombre

        self.apellido = apellido

# primera vista


def saludo(request):

    p1=Persona("Javier", "Aguayo")

    nombre = "Hugo"

    apellido = "Rocha"

    ahora = datetime.datetime.now()

    # Para darle formato a las cosas simplemnte se crea una variable en el cual abrimos el documento
    doc_externos = open(
        "C:/Users/chama/Desktop/Course_Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externos.read())

    doc_externos.close()

    # Contexto es el argumento para el render, en el cual podemos guardar diccionarios para poder usar estructuras o variables
    # En el argumento del contexto pasamos las variables al igual se puede dar el valor en el mismo contexto
    ctx = Context({"nombre_persona": p1.nombre,
                   "apellido_persona": p1.apellido, 
                   "fecha": ahora,
                   })

    documento = plt.render(ctx)

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
