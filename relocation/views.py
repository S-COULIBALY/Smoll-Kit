from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Demenagement
from .forms import *
# Create your views here.
def home(request):
    dem_form = DemenagementForm()
    option_form = OptionSupplementaireForm()
    address_form = AddressForm()
    option_supplementaire_form = OptionSupplementaireForm()

    context = {
        'dem_form': dem_form,
        #'option_form': option_form,
        'address_form': address_form,
        'option_supplementaire_form': option_supplementaire_form
        }
    return render(request, "relocation/home.html", context)


def detail(request):
    item= request.POST
    context = {
        'item': item
        }
    return render(request, 'relocation/detail.html', context)










"""
class ProspectCreateView(FormView):
    template_name=  "relocation/home.html"
    form_class = DemenagementForm
    #success_url = '/thanks/'
"""