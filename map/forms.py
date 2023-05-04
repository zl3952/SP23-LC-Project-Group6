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
        ('', 'Select a field'),
        ('Bronx', 'Bronx'),
        ('Brooklyn', 'Brooklyn'),
        ('Manhattan', 'Manhattan'),
        ('Queens', 'Queens'),
        ('Staten Island', 'Staten Island'),
    ], initial = '', required=True)
    geo_type_name = forms.ChoiceField(choices=[
        ('', 'Select a area type'),
        ('Borough', 'Borough'),
    ], initial = '', required=True)