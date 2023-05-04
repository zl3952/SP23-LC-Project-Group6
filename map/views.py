from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.views import View

from .models import NYCData




def maps(request):
    data = NYCData

    context = {
        #"name": name,
    }
    return render(request, "map.html", context)
