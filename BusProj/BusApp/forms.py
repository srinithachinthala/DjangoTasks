from django import forms
from .models import BusTable
class BusForm(forms.ModelForm):
    class Meta:
        model=BusTable
        fields='__all__'