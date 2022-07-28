"""This is a docstring which describes the module"""
from django.forms import ModelForm
from recipesite.models import IngredientLists


class IngredientListsForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = IngredientLists
        fields = [
            'ingredient',
            'unitId',
            'quantity',
            'description'
        ] 
