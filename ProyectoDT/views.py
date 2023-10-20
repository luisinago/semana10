from django.http import HttpResponse
import datetime
from django.template import loader

def dia_template(request):
    dia = datetime.datetime.now()
    #Cómo hacer para mostrar solo los datos que se muestran en la imagen?
    plantilla = loader.get_template("index.html")
    documento = plantilla.render(dia)
    return HttpResponse(documento)