from django.db import models
from django.contrib.auth.models import User

class Pet(models.Model):
    pet_name = models.CharField(max_length=200)
    species = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    weight_in_pounds = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.pet_name

class Appointment(models.Model):
    date_of_appointment = models.DateField()
    duration_minutes = models.IntegerField(help_text="Time in minutes")
    special_instructions = models.CharField(max_length=500,help_text="Any special requests", null=True, blank=True, default="None")
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT, blank=True, null=True)



