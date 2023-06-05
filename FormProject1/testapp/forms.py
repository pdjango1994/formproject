from django import forms

class BeerForm(forms.Form):
    name=forms.CharField()
    price=forms.FloatField()
    
