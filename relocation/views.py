from django.shortcuts import render
from django.template import loader

# Create your views here.

from django.http import HttpResponse
from .models import Demenagement
from datetime import datetime

def index(request):
    relocation_date = ''
    template = loader.get_template('relocation/new.html')
    context = {}
    relocation = Demenagement()
    return render(request, 'relocation/new.html', context)


def create(request):
    print(request.POST['relocation_heure'])

    relocation_date = datetime.strptime(request.POST['relocation_date'], '%Y-%m-%d').date()
    relocation_heure = datetime.strptime(request.POST['relocation_heure'], '%H:%M').time()
    comment =  request.POST['comment']
    volume =  request.POST['volume']

    relocation = Demenagement()
    relocation.relocation_date = datetime.combine(relocation_date, relocation_heure)
    relocation.comment = comment
    relocation.volume = volume

    relocation.save()

    context = {'relocation_date': relocation_date}
    return render(request, 'relocation/create.html', context)
