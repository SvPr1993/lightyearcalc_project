import unicodedata
from django import forms
from .models import DataCalc


class DataCalcForm(forms.ModelForm):
    class Meta:
        model = DataCalc
        fields = ("planet_name", "destination_sum")

    def clean_username(self):
        planet_name = self.cleaned_data['planet_name']
        return unicodedata.normalize('NFKC', planet_name).upper().strip()
