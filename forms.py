__author__ = 'Elliot Hutchins'
from django import forms
from django.forms.formsets import formset_factory
from .models import chipCalculate, chipInput



class ChipCalculate(forms.ModelForm):
    class Meta:
        model = chipCalculate


class chipinput_form(forms.ModelForm):
    class Meta:
        model = chipInput
        fields = ['chip_color', 'chips_worth', 'number_of_this_chip', 'active', 'per_person']


active_chips = chipInput.objects.active().values()
display_chip_formset = formset_factory(chipinput_form, extra=10)
chip_set = display_chip_formset(initial=[active_chips]
)


for form in chip_set:
    print (form.as_table())







