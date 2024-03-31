from django import forms

class UpdateForm(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    weight = forms.FloatField()
    height = forms.FloatField()
    gender_choices = [('male', 'Male'), ('female', 'Female'), ('other', 'Other')]
    gender = forms.ChoiceField(choices=gender_choices)
    alcohol_choices = [('yes', 'Yes'), ('no', 'No')]
    alcohol = forms.ChoiceField(choices=alcohol_choices)
    trisemister_choices = [('first', 'First'), ('second', 'Second'), ('third', 'Third'), ('None', 'None')]
    trisemister = forms.ChoiceField(choices=trisemister_choices)

class LocationForm(forms.Form):
    locationOption_choices = [('currentLocation', 'Current Location'), ('writtenLocation', 'Enter Location')]
    locationOption = forms.ChoiceField(choices=locationOption_choices)
    locationInput = forms.CharField(required=False)
    hospitalRange_choices = [(i, i) for i in range(1, 11)]
    hospitalRange = forms.ChoiceField(choices=hospitalRange_choices)
