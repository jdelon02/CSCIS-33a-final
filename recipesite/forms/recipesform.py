"""This is a docstring which describes the module"""
from django.forms import ModelForm, inlineformset_factory
from recipesite.models import Recipes, IngredientLists


class RecipesForm(ModelForm):
    """This is a docstring which describes the module"""
    
    class Meta:
        """This is a docstring which describes the module"""
        model = Recipes
        fields = [
            'name',
            'description',
            'servingQuantity',
            'skillLevel',
            'prepTimeHour',
            'prepTimeMin',
            'cookTimeHour',
            'cookTimeMin'
            # 'ingredients_list'
        ]
        exclude = ('ingredients_list')
IngredientFormSet = inlineformset_factory(IngredientLists, Recipes, form=RecipesForm)