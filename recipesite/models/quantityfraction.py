"""This is a docstring which describes the module"""
from django import forms
from django.forms import ModelForm
from django.db.models import (
    Model,
    CharField
)


class QuantityFraction(Model):

    quantFraction = CharField(
        max_length = 8
    )
    