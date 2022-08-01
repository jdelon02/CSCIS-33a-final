""" This is a docstring which describes the module """
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import DateTimeField


class User(AbstractUser):
    """ This is a docstring which describes the model """
    date_joined = DateTimeField(
        auto_now_add=True,
        blank=True
    )
    last_login = DateTimeField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.id

    def serialize(self):
        return {
            "id": self.id
        }