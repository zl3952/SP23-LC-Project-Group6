from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from .filters import Filter
from .models import NYCData
from .forms import SearchForm
import requests

def nyc_data_view(request):
    form = SearchForm(request.GET)
    data = []
    if form.is_valid():
        search_term = form.cleaned_data['search_term']
        search_field = form.cleaned_data['search_field']
        url = 'https://data.cityofnewyork.us/resource/c3uy-2p5r.json'
        params = {search_field: search_term}
        response = requests.get(url, params=params)
        data = response.json()
    return render(request, 'map.html', {'data': data, 'form': form})


#def maps(request):
#    map_filter = Filter(request.GET, queryset=NYCData.objects.all())
#    context = {"form": map_filter.form, "maps": map_filter.qs}
#    return render(request, "map.html", context)
