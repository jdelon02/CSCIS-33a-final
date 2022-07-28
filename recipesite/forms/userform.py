"""This is a docstring which describes the module"""
from curses.ascii import US
from django.forms import ModelForm
from recipesite.models import User


class RecipePostForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = User
        fields = ['body']