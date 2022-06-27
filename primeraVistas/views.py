
from unicodedata import name
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

from primeraVistas.models import Person


def index(request):
    people = Person.objects.all()
    template = loader.get_template('index.html')
    context = {'people': people, }

    person_1 = Person(name="Fabian", last_name="Borsato",
                      email="borsatofabian@gmail.com", date_of_birth="1965-11-25", city="Mar de ajo")

    render = template.render({'person_1': person_1})

    return HttpResponse(render)


def family_list(request):

    template = loader.get_template('family_list.html')

    people_list = Person.objects.all()
    render = template.render({"people_list": people_list})

    return HttpResponse(render)

def mi_template(request, nombre):

    template1 = loader.get_template('index.html')

    render1 = template1.render({'nombre': nombre})

    return HttpResponse(render1)
