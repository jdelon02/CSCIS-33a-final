"""This is a docstring which describes the module"""
from django import forms
from django.forms import ModelForm, CharField
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from recipesite.models import QuantityFraction


class QuantityFractionForm(ModelForm):
    """This is a docstring which describes the module"""
    QUANTS = Choices(
        ('quantity', _('Quantity')),
        ('1/4', _('1/4')),
        ('1/3', _('1/3')),
        ('1/2', _('1/2')),
        ('2/3', _('2/3')),
        ('3/4', _('3/4')),
    )
    
    quantFraction = CharField(
        max_length = 8,
        choices=QUANTS        
    )
    
    class Meta:
        """This is a docstring which describes the module"""
        model = QuantityFraction
        fields = ['quantFraction']
    
    def __str__(self):
        return self.quantFraction
           
    def __init__(self, *args, **kwargs):
        super(QuantityFractionForm, self).__init__(*args, **kwargs)
        