from django.shortcuts import render_to_response, RequestContext
from django.forms.models import modelformset_factory, formset_factory


from .ChipCalculatorV02 import final_list
from .forms import ChipCalculate, chipinput_form
from .models import chipInput, chipCalculate





def chipcalculate(request):

    # Forms to POST
    chipcalc = ChipCalculate(request.POST or None, prefix='calculate')
    chipsubmit = chipinput_form(request.POST or None)

    # load the previous settings
    prev_settings = chipCalculate.objects.get(user='anon')
    display_saved_total = chipCalculate.objects.filter(user='anon').values('calculated_total')[0].values()[0]
    display_prev_chipvalue = chipCalculate.objects.filter(user='anon').values('prev_chip_value')[0].values()[0]
    display_prev_players = chipCalculate.objects.filter(user='anon').values('number_of_players')[0].values()[0]

    # Model References
    all_chips = chipInput.objects.all().values()


    # Formset with initial values
    display_chip_formset = modelformset_factory(chipInput, chipinput_form, extra=(1), max_num=9, can_delete=True)
    chip_set = display_chip_formset(request.POST or None)


    if request.method == 'POST':
        active_chips = chipInput.objects.active().values()



        if chipcalc.is_valid():

            # Create list of items to put into the chipcalculator
            list = []
            for each in active_chips:
                lista = []
                lista.append(each['chip_color'])
                lista.append(each['number_of_this_chip'])
                lista.append(each['chips_worth'])
                list.append(lista)


            # run through chip calculator with items in the DB
            final_list_calculated = final_list(int(request.POST.getlist('calculate-chip_total_value')[0]),
                                               int(request.POST.getlist('calculate-number_of_players')[0]), list)

            # the true total from the calculator
            true_total = final_list_calculated[1]
            # number of chips per player after these objects have been run through the calculator
            advised_chips = final_list_calculated[0]

            # save chips per person to DB
            for each in advised_chips:
                chip_input = chipInput.objects.get(chip_color=each[1])
                per_person = chip_input.per_person
                per_person = each[0]
                chip_input.per_person = per_person
                chip_input.save()

            # save the current settings to the DB
            prev_settings.calculated_total = true_total
            prev_settings.save()

            # re-pull items from the newly saved database
            display_saved_total = chipCalculate.objects.filter(user='anon').values('calculated_total')[0].values()[0]

            # re-declare variables after saving, to initialize form with the new per-person amounts
            active_chips = chipInput.objects.active().values()
            chip_set = display_chip_formset()

            # return final
            return render_to_response("chipcalculated.html", locals(), context_instance=RequestContext(request))

        if chip_set.is_valid():
            chip_set_save = chip_set.save(commit=True)
            chip_set.save()

            # re-declare variables after saving, to initialize form with the new chips
            active_chips = chipInput.objects.active().values()
            chip_set = display_chip_formset()

    return render_to_response("chipcalculated.html", locals(), context_instance=RequestContext(request))








