from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import NYCData

def maps(generic.ListView):
    model = NYCdata
    template_name = 'map/map.html'