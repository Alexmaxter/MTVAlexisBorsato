
from unicodedata import name
from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

from primeraVistas.models import Person


def index(request):
    template = loader.get_template('index.html')

    render = template.render({})

    return HttpResponse(render)


def family_list(request):

    people_list = Person.objects.all()
    template = loader.get_template('family_list.html')

    person_1 = Person(name="Fabian", last_name="Borsato",
                      email="borsatofabian@gmail.com", date_of_birth="1965-11-25", city="Mar de ajo")

    person_2 = Person(name="Liliana", last_name="Vidla",
                      email="vidlaliliana@gmail.com", date_of_birth="1961-04-02", city="Oberá")

    person_3 = Person(name="Beatriz", last_name="Alencastro",
                      email="alencastrobeatriz@gmail.com", date_of_birth="1936-11-28", city="Concordia")

    render = template.render({"people_list": people_list})

    return HttpResponse(render)
