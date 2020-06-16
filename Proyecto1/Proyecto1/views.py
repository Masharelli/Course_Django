from django.http import HttpResponse
import datetime
from django.template import Template, Context

# primera vista

def saludo(request):
    # Para darle formato a las cosas simplemnte se crea una variable
    doc_externos = open("C:/Users/chama/Desktop/Course_Django/Proyecto1/Proyecto1/plantillas/miplantilla.html")

    plt = Template(doc_externos.read())

    doc_externos.close()

    # Entonces simplemente le pedimos al return que regrese esta variablee
    ctx = Context()

    documento = plt.render(ctx)

    return HttpResponse(documento)


def despedida(request):
    return HttpResponse("Gracias por visitar esta pagina")

#Esto regresa la fecha actual
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
    """ %(agno, edadFutura)

    return HttpResponse(documento)
