"""This is a docstring which describes the module"""
from django.forms import ModelForm
from recipesite.models import Food


class FoodForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Food
        fields = ['name']

    def __str__(self):
        return self.name
            
    def __init__(self, *args, **kwargs):
        super(FoodForm, self).__init__(*args, **kwargs)