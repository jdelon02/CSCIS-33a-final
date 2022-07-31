"""This is a docstring which describes the module"""
from django.forms import ModelForm
from recipesite.models import Difficulty


class DifficultyForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Difficulty
        fields = ['level']
    
    def __str__(self):
        return self.level
           
    def __init__(self, *args, **kwargs):
        super(DifficultyForm, self).__init__(*args, **kwargs)
        