__author__ = 'Elliot Hutchins'
from django import forms

from .models import chipCalculate, chipInput



class ChipCalculate(forms.ModelForm):
    class Meta:
        model = chipCalculate
        fields = ['chip_total_value', 'number_of_players']


class chipinput_form(forms.ModelForm):
    class Meta:
        model = chipInput
        fields = ['chip_color', 'chips_worth', 'number_of_this_chip', 'active', 'per_person']












