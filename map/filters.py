import django_filters.filterset
from map.models import NYCData


class Filter(django_filters.FilterSet):
    class Meta:
        model = NYCData
        fields = {
            "geo_place_name": ["exact"],
            "name": ["exact"],
        }
