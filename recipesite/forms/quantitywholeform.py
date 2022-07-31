"""This is a docstring which describes the module"""
from django import forms
from django.forms import ModelForm, CharField
from recipesite.models import QuantityWhole


class QuantityWholeForm(ModelForm):
    """This is a docstring which describes the module"""
    
    quantWhole = CharField(
        max_length = 2       
    )
    
    class Meta:
        """This is a docstring which describes the module"""
        model = QuantityWhole
        fields = ['quantWhole']
    
    def __str__(self):
        return self.quantWhole
           
    def __init__(self, *args, **kwargs):
        super(QuantityWholeForm, self).__init__(*args, **kwargs)
        