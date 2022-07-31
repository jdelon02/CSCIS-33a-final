"""This is a docstring which describes the module"""
from django import forms
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.forms import ModelForm, inlineformset_factory
from recipesite.models import Recipes, Ingredients


class RecipesForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Recipes
        fields = [
            'name',
            'description'
        ]
    
    def __str__(self):
        return self.name
        
    def __init__(self, *args, **kwargs):
        super(RecipesForm, self).__init__(*args, **kwargs)
        
        DIFFS = Choices(
            ('default', _('Difficulty')),
            ('easy', _('Easy')),
            ('medium', _('Medium')),
            ('hard', _('Hard')),
        )
        SERVING = Choices(
            ('serving_size', _('Serving Size')),
            ('2', _('2')),
            ('4', _('4')),
            ('6', _('6')),
            ('8', _('8')),
            ('8+', _('More than 8')),
        )
        HOURSTATUS = Choices(
            ('hrs', _('Hours')),
            ('1', _('1')),
            ('2', _('2')),
            ('3', _('3')),
            ('4', _('4')),
            ('5', _('5')),
            ('6', _('6')),
            ('7', _('7')),
            ('8', _('8')),
            ('9', _('9')),
            ('10', _('10')),
            ('11', _('11')),
            ('12', _('12')),
        )
        MINSTATUS = Choices(
            ('mins', _('Minutes')),
            ('00', _('00')),
            ('15', _('15')),
            ('30', _('30')),
            ('45', _('45')),
        )
        self.fields['skillLevel'] = forms.ChoiceField(choices=DIFFS)
        self.fields['servingQuantity'] = forms.ChoiceField(choices=SERVING)
        self.fields['prephour'] = forms.ChoiceField(choices=HOURSTATUS)
        self.fields['prepmin'] = forms.ChoiceField(choices=MINSTATUS)
        self.fields['cookhour'] = forms.ChoiceField(choices=HOURSTATUS)
        self.fields['cookmin'] = forms.ChoiceField(choices=MINSTATUS)

IngredientFormSet = inlineformset_factory(
    Recipes, 
    Ingredients,
    fields=(
        'quantitywhole',
        'quantityfraction',
        'unitId',
        'name',
        'description'
    ),
    extra=1,
    can_delete=True
)
