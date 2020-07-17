from django.test import TestCase
from django.contrib.auth.models import User

from pets.models import Pet, Appointment

class PetTestCase(TestCase):
    
    def test_homepage(self):
        user = User.objects.create()

        Pet.objects.create(pet_name="Dave", species='Dog',breed='Corgi',)