from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from miapp.models import familiares

#Falta crear los path para visualizar desde la BD

def plant_familia(request):

    mifamilia = familiares.objects.all()

    datos = {"mifamilia": mifamilia}

    plantilla = loader.get_template("template_familia.html")

    documento = plantilla.render(datos)

    return HttpResponse(documento)