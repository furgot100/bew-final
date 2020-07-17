from django.shortcuts import render
from .models import Pet, Appointment
from .forms import PetCreateForm, CalenderCreateForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic


def home(request):
    context = {
        'pets' : Pet.objects.all()
    }
    return render(request, 'home.html', context)

def detail(request,pet_id):
    context = {
        'dates' : Appointment.objects.filter(pet=pet_id),
        'pet' : Pet.objects.get(id=pet_id)
    }

    return render(request, 'detail.html', context)

def calender(request):
    context = {
        'dates': Appointment.objects.all(),
    }
    return render(request,'calender.html', context)


class PetCreateView(generic.edit.CreateView):  
    login_url = reverse_lazy('login')
    
    def get(self, request, *args, **kwargs):
        context = {
          'form': PetCreateForm()
        }
        return render(request, 'create.html', context)

    def post(self, request, *args, **kwargs):
        form = PetCreateForm(request.POST)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return HttpResponseRedirect(
                reverse('pets:pet-detail', args=[pet.id]))
        # else if form is not valid
        return render(request, 'create.html', { 'form': form })

class CalenderCreateViews(generic.edit.CreateView):
    login_url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        context = {
            'form' : CalenderCreateForm()
        }
        return render(request, 'create_calender.html',  context)

    def post(self, request, *args, **kwargs):
        form = CalenderCreateForm(request.POST)
        if form.is_valid():
            date = form.save(commit=False)
            date.save()
            return HttpResponseRedirect(
                reverse('pets:calender')
            )
        return render(request, 'create_calender.html', {'form': form})
    

    