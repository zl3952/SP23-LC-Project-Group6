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
        #search_term = form.cleaned_data['search']
        #search_field = form.cleaned_data['field']
        geo_type_name = form.cleaned_data['geo_type_name']
        geo_place_name = form.cleaned_data['geo_place_name']
        url = 'https://data.cityofnewyork.us/resource/c3uy-2p5r.json'
        #params = {'$where': f"{search_field} like '%{search_term}%'"}
        params = {}
        if geo_type_name:
        	params['geo_type_name'] = geo_type_name
        if geo_place_name:
        	params['geo_place_name']= geo_place_name
        response = requests.get(url, params=params)
        data = response.json()
    return render(request, 'map.html', {'data': data, 'form': form})


#def maps(request):
#    map_filter = Filter(request.GET, queryset=NYCData.objects.all())
#    context = {"form": map_filter.form, "maps": map_filter.qs}
#    return render(request, "map.html", context)
