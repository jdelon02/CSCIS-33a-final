"""This is a docstring which describes the module"""
from django.forms import ModelForm
from django.db.models import (
    Model,
    CharField
)


class PrepCookMin(Model):
    
    timeMin = CharField(
        max_length=7
    )
    