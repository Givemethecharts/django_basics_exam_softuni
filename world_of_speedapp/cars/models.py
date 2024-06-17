from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speedapp.cars.validators import validate_car_year
from world_of_speedapp.profiles.models import Profile

# Create your models here.
CAR_TYPE_CHOICES = (('Rally', 'Rally'),
                    ('Open-wheel', 'Open-wheel'),
                    ('Kart', 'Kart'),
                    ('Drag', 'Drag'),
                    ('Other', 'Other'),)


class Car(models.Model):
    type = models.CharField(max_length=10,
                            blank=False,
                            null=False,
                            choices=CAR_TYPE_CHOICES)

    model = models.CharField(max_length=15,
                             blank=False,
                             null=False,
                             validators=[MinLengthValidator(1)])

    year = models.IntegerField(blank=False,
                               null=False,
                               validators=[validate_car_year])

    image_url = models.URLField(blank=False,
                                null=False,
                                unique=True,
                                )
    price = models.FloatField(blank=False,
                              null=False,
                              validators=[MinValueValidator(1.0)])

    owner = models.ForeignKey(to=Profile, on_delete=models.CASCADE, editable=False)