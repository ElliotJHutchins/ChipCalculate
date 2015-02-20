from django.db import models




class chipCalculate(models.Model):
    chip_value_choices = ((200, 200), (500, 500), (1000, 1000), (2000, 2000),
                          (3000, 3000), (5000, 5000), (10000, 10000), (20000, 20000))
    chip_total_value = models.IntegerField(default=2000, choices=chip_value_choices)
    number_of_players = models.IntegerField(default=8)



class chipInput_active(models.Manager):
    def active(self):
        return self.get_queryset().filter(active=True, user='anon')




class chipInput(models.Model):
    chip_color = models.CharField(max_length=18, default='', unique=True)
    chip_worth_choices = ((1, 1), (5, 5), (10, 10), (25, 25),
                          (50, 50), (100, 100), (500, 500), (1000, 1000), (5000, 5000))
    chips_worth = models.IntegerField(default=5, choices=chip_worth_choices, unique=True)
    number_of_this_chip = models.IntegerField(default=200)
    active = models.BooleanField(default=True)
    user = models.CharField(max_length=10, default='anon')
    per_person = models.IntegerField(default=0)
    objects = chipInput_active()







