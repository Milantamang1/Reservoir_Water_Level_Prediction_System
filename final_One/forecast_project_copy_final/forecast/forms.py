from django import forms

class PredictionForm(forms.Form):
    field1 = forms.FloatField(required=True)
    field2 = forms.FloatField(required=True)
    field3 = forms.FloatField(required=True)
    field4 = forms.FloatField(required=True)
    field5 = forms.FloatField(required=True)
