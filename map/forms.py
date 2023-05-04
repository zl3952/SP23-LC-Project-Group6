from django import forms

class SearchForm(forms.Form):
    search_term = forms.CharField(required=False)
    search_field = forms.ChoiceField(choices=[
        ('geo_place_name', 'Geo Name'),
        ('data_value', 'Data Value'),
        ('name', 'Particle Type'),
    ])