from django.shortcuts import render

from world_of_speedapp.profiles.models import Profile


def profile_context(request):
    profile = Profile.objects.first()
    return {'profile': profile}


# Create your views here.

def index(request):
    return render(request, template_name='web/index.html', )
