from django.http import HttpResponse
from .models import Plato
from django.template import loader




def index(request):
    platos_list = Plato.objects.all()
    template = loader.get_template("restaurante/platos.html")
    context = {
        "lista_platos": platos_list,
    }
    return HttpResponse(template.render(context, request))