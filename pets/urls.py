from django.urls import path

from . import views

app_name = 'pets'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:pet_id>/', views.detail, name='pet-detail'),
    path('create/', views.PetCreateView.as_view(), name='create'),
    path('calander/', views.calender, name='calender'),
    path('calander/create/', views.CalenderCreateViews.as_view(), name="calender-create")
]