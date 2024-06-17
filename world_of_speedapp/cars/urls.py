from django.urls import path

from world_of_speedapp.cars import views

urlpatterns = (path('catalogue/', views.catalogue_page, name='catalogue-page'),
               path('create/', views.create_car, name='create-car'),
               path('<int:id>/details/', views.car_details, name='car-details'),
               path('<int:id>/edit/', views.car_edit, name='car-edit'),
               path('<int:id>/delete/', views.car_delete, name='car-delete'))