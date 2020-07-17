from django import forms

from .models import Pet, Appointment

class PetCreateForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['pet_name', 'species', 'breed','weight_in_pounds']

class CalenderCreateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date_of_appointment', 'duration_minutes', 'special_instructions','pet']