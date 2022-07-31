"""This is a docstring which describes the module"""
from django.forms import ModelForm
from recipesite.models import Bookmarks


class BookmarksForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Bookmarks
        fields = ['recipes']
    
    def __str__(self):
        return self.recipes
        
    def __init__(self, *args, **kwargs):
        super(BookmarksForm, self).__init__(*args, **kwargs)