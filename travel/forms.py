from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['first_name', 'place_name', 'date', 'photo', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }