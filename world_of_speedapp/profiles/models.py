from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from world_of_speedapp.profiles.validators import validate_name


# Create your models here.
class Profile(models.Model):
    username = models.CharField(max_length=15,
                                blank=False,
                                null=False,
                                validators=[MinLengthValidator(3, 'Username must be at least 3 chars long!'),
                                            validate_name])

    email = models.EmailField(blank=False,
                              null=False)

    age = models.IntegerField(blank=False,
                              null=False,
                              validators=[MinValueValidator(21)],
                              )

    password = models.CharField(max_length=20,
                                blank=False,
                                null=False)

    first_name = models.CharField(max_length=25,
                                  blank=True,
                                  null=True)

    last_name = models.CharField(max_length=25,
                                 blank=True,
                                 null=False)

    profile_picture = models.URLField(blank=True,
                                      null=True)
