from django.shortcuts import render, redirect

from world_of_speedapp.cars.forms import CarCreateForm, CarDeleteForm
from world_of_speedapp.cars.models import Car
from world_of_speedapp.profiles.models import Profile


# Create your views here.

def catalogue_page(request):
    cars = Car.objects.filter(owner=Profile.objects.first())
    context = {'cars': cars}
    return render(request, template_name='cars/catalogue.html', context=context)


def create_car(request):
    if request.method == "POST":
        form = CarCreateForm(request.POST or None)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = Profile.objects.first()
            car.save()
            return redirect('catalogue-page')
    else:
        form = CarCreateForm()

    context = {'form': form}
    return render(request, template_name='cars/car-create.html', context=context)


def car_details(request, id):
    car = Car.objects.get(pk=id)
    context = {'car': car}
    return render(request, template_name='cars/car-details.html', context=context)


def car_edit(request, id):
    car = Car.objects.get(pk=id)
    if request.method == "POST":
        form = CarCreateForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue-page')
    else:
        form = CarCreateForm(instance=car)
    context = {'form': form}
    return render(request, template_name='cars/car-edit.html', context=context)


def car_delete(request, id):
    car = Car.objects.get(pk=id)
    if request.method == "POST":
        car.delete()
        return redirect("catalogue-page")
    else:
        form = CarDeleteForm(instance=car)
    context = {'form': form}
    return render(request, template_name='cars/car-delete.html', context=context)
