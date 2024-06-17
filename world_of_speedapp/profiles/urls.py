from django.urls import path

from world_of_speedapp.profiles import views
from world_of_speedapp.profiles.views import DeleteProfileView

urlpatterns = (path('create', views.sing_up, name='create-profile'),
               path('details/', views.profile_details, name='profile-details'),
               path('edit/', views.profile_edit, name='profile-edit'),
               path('delete/', DeleteProfileView.as_view(), name='profile-delete'))
