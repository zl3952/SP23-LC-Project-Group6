from django import forms

class SearchForm(forms.Form):
    #search = forms.CharField(required=False)
    # field = forms.ChoiceField(choices=[
    #     ('', 'Select a field'),
    #     ('geo_place_name', 'Geo Name'),
    #     ('data_value', 'Data Value'),
    #     ('name', 'Particle Type'),

    # ], initial = '')
    geo_place_name = forms.ChoiceField(choices=[
        ('', 'Select a borough'),
        ('Bronx', 'Bronx'),
        ('Brooklyn', 'Brooklyn'),
        ('Manhattan', 'Manhattan'),
        ('Queens', 'Queens'),
        ('Staten Island', 'Staten Island'),
    ], initial = '', required=True, label = "Borough")
    geo_type_name = forms.ChoiceField(choices=[
        ('', 'Select a area type'),
        ('Borough', 'Borough'),
    ], initial = '', required=True, label = "Area Type")
    name = forms.ChoiceField(choices = {
        ('', 'Select a pollutant type'),
        ('Ozone (O3)', 'Ozone (O3)'),
        ('Air Toxics Concentrations', 'Air Toxics Concentrations'),
        ('Fine Particulate Matter (PM2.5)','PM2.5'),
        ('SO2', 'Sulfur Dioxide (SO2)'),
        ('NO2', 'Nitrogen Dioxide (NO2)'),
        ('Traffic', 'Traffic Density'),

    }, initial = '', required=True, label = "Pollutant")