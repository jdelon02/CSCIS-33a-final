"""This is a docstring which describes the module"""
from django.forms import ModelForm
from recipesite.models import Ingredients


class IngredientsForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Ingredients
        fields = ['name']