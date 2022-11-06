from django.http import HttpResponse
from django.template import Template, Context, loader
   
def vista_inicio(request):

    plantilla = loader.get_template("template.html")
    documento = plantilla.render()
    return HttpResponse(documento)