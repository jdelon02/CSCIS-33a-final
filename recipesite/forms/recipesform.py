"""This is a docstring which describes the module"""
from django import forms
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.forms import ModelForm, inlineformset_factory, ChoiceField, Select
from recipesite.forms.ingredientsform import IngredientsForm
from recipesite.models import Recipes, Ingredients
from easy_select2 import select2_modelform, Select2


class RecipesForm(ModelForm):
    """This is a docstring which describes the module"""
    QUANTS = Choices(
        ('1/4', _('1/4')),
        ('1/3', _('1/3')),
        ('1/2', _('1/2')),
        ('2/3', _('2/3')),
        ('3/4', _('3/4')),
    )
    class Meta:
        """This is a docstring which describes the module"""
        model = Recipes
        fields = [
            'name',
            'description',
            'likes'
        ]
    
    def __str__(self):
        return self.name
    
    @property
    def total_likes(self):
        return self.likes.count() 
    
    def serialize(self):
        return {
            "id": self.id,
            # Originally, I had user included, but serialization breaks with foreign keys.
            # "user_id": self.user_id,
            "name": self.name,
            "description": self.description,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "likes": self.likes.count()
        }
        
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
        self.fields['skillLevel'] = forms.ChoiceField(
                                widget=Select2(),
                                choices=DIFFS, 
                                label="Skill Level"
                        )
        self.fields['servingQuantity'] = forms.ChoiceField(
                                choices=SERVING, 
                                label="Servings / Quantity"
                        )
        self.fields['prephour'] = forms.ChoiceField(
                                choices=HOURSTATUS, 
                                label="Hours"
                        )
        self.fields['prepmin'] = forms.ChoiceField(
                                choices=MINSTATUS, 
                                label="Minutes"
                        )
        self.fields['cookhour'] = forms.ChoiceField(
                                choices=HOURSTATUS, 
                                label="Hours"
                        )
        self.fields['cookmin'] = forms.ChoiceField(
                                choices=MINSTATUS, 
                                label="Minutes"
                        )

IngredientFormSet = inlineformset_factory(
    Recipes, 
    Ingredients,
    # fields=(
    #     'quantitywhole',
    #     'quantityfraction',
    #     'unitId',
    #     'name',
    #     'description'
    # ),
    form=IngredientsForm,
    extra=1,
    can_delete=True
)
