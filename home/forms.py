from django import forms
from .models import ElectricityStatus

class ElectricityForm(forms.ModelForm):
    class Meta:
        model = ElectricityStatus
        fields = ['name', 'email', 'has_electricity']