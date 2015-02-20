from django.shortcuts import render, render_to_response, RequestContext


from django.shortcuts import get_object_or_404
from .ChipCalculatorV02 import final_list
from .forms import ChipCalculate, chipinput_form, chip_set
from .models import chipInput





def chipcalculate(request):

    chip_table = chip_set
    chipcalc = ChipCalculate(request.POST or None)
    chipsubmit = chipinput_form(request.POST or None)
    all_chips = chipInput.objects.all().values
    advised_chips = []




    if chipsubmit.is_valid():
        save_submit = chipsubmit.save(commit=True)
        save_submit.save

    if chip_table.is_valid():
        save_submit1 = chip_table.save(commit=True)
        save_submit1.save



    if chipcalc.is_valid():

        advised_chips = final_list(int(request.POST.getlist('chip_total_value')[0]), int(request.POST.getlist('number_of_players')[0]))


        return render_to_response("chipTable.html", locals(), context_instance=RequestContext(request))

    return render_to_response("chipTable.html", locals(), context_instance=RequestContext(request))






