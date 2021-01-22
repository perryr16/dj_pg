from django.shortcuts import render
from cars.models import Car, Driver
# Create your views here.
def car_detail(request, pk):
  owner_obj = Driver.objets.get(pk=pk)
  car_objs = Car.objects.filter(owner_id=owner_obj.id)
  context = {
    "vehicles": car_objs,
    "drivers": owner_objs,
  }
  return render(request, "car_detail.html", context)