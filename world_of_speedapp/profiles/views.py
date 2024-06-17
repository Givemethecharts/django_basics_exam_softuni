from django.shortcuts import render, redirect

from world_of_speedapp.cars.models import Car
from world_of_speedapp.profiles.forms import ProfileCreateForm, ProfileEditForm
from world_of_speedapp.profiles.models import Profile

from django.views import generic as views
from django.urls import reverse_lazy


# Create your views here.

def get_profile():
    return Profile.objects.first()


def sing_up(request):
    if request.method == "POST":
        form = ProfileCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('catalogue-page')
    else:
        form = ProfileCreateForm()

    context = {'form': form}
    return render(request, template_name='profiles/profile-create.html', context=context)


def profile_details(request):
    profile = get_profile()
    cars = Car.objects.filter(owner=profile)
    total_price = sum(car.price for car in cars)
    context = {'profile': profile,
               'total_price': total_price}
    return render(request, template_name='profiles/profile-details.html', context=context)


def profile_edit(request):
    profile = get_profile()
    if request.method == "POST":
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile-details')
    else:
        form = ProfileEditForm(instance=profile)
    context = {'form': form}
    return render(request, template_name='profiles/profile-edit.html', context=context)


class DeleteProfileView(views.DeleteView):
    template_name = 'profiles/profile-delete.html'
    success_url = reverse_lazy('home-page')

    def get_object(self, queryset=None):
        return get_profile()
