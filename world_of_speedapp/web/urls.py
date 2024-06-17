from django.urls import path

from world_of_speedapp.web import views

urlpatterns = (path('', views.index, name='home-page'),)