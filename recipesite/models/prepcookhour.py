"""This is a docstring which describes the module"""
from django.forms import ModelForm
from django.db.models import (
    Model,
    CharField
)


class PrepCookHour(Model):
    
    timeHour = CharField(
        max_length = 8
    )
    