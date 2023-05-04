from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
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
        name = form.cleaned_data['name']
        url = 'https://data.cityofnewyork.us/resource/c3uy-2p5r.json'
        #params = {'$where': f"{search_field} like '%{search_term}%'"}
        params = {}
        if geo_type_name:
        	params['geo_type_name'] = geo_type_name
        if geo_place_name:
        	params['geo_place_name'] = geo_place_name
        if name:
        	params['$where'] = f"name like '%{name}%'"
        response = requests.get(url, params=params)
        data = response.json()
        max_value = max(float(d['data_value']) for d in data)
        min_value = min(float(d['data_value']) for d in data)
        data_values = [float(d['data_value']) for d in data]
        avg_value = sum(data_values) / len(data_values) if data_values else 0

    return render(request, 'map.html', {'data': data, 'form': form, 'max_value': max_value, 'geo_place_name': geo_place_name, 'min_value': min_value, 'avg_value': avg_value, 'name':name})


#def maps(request):
#    map_filter = Filter(request.GET, queryset=NYCData.objects.all())
#    context = {"form": map_filter.form, "maps": map_filter.qs}
#    return render(request, "map.html", context)
