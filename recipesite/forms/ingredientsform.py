"""This is a docstring which describes the module"""
from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from recipesite.models.ingredients import Ingredients


class IngredientsForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Ingredients
        fields = [
            'name',
            'description'
        ]
        
    def __str__(self):
        return self.name

    def __init__(self, *args, **kwargs):
        super(IngredientsForm, self).__init__(*args, **kwargs)
        UNITSTATUS = Choices(
            ('unit', ('Unit')),
            ('cup', ('Cup')),
            ('tablespoon', ('Tablespoon')),
            ('teaspoon', ('Teaspoon')),
            ('pint', ('Pint')),
            ('quart', ('Quart')),
            ('ounce', ('Ounce')),
            ('dozen', ('Dozen')),
            ('can', ('Can')),
            ('bunch', ('Bunch')),
            ('whole', ('Whole')),
        )
        QUANTS = Choices(
            ('quantity', _('Quantity')),
            ('1/4', _('1/4')),
            ('1/3', _('1/3')),
            ('1/2', _('1/2')),
            ('2/3', _('2/3')),
            ('3/4', _('3/4')),
        )
        self.fields['unitId'] = forms.ChoiceField(choices=UNITSTATUS)
        self.fields['quantityfraction'] = forms.ChoiceField(choices=QUANTS)

        
