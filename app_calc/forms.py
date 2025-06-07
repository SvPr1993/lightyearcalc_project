from django import forms
from .models import DataCalc


class DataCalcForm(forms.ModelForm):
    class Meta:
        model = DataCalc
        fields = ("planet_name", "destination_sum")
