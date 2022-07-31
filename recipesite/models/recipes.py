"""Data models."""
from django.db import models
from django.urls import reverse
# from .ingredientlists import IngredientLists
# from .ingredients import Ingredients
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    TextField,
    ManyToManyField,
    CharField
)
from . import User, ServingSize, PrepCookMin, PrepCookHour, Difficulty, Ingredients

# TODO: Description Field to model, recipe.
class Recipes(Model):
    
    """Data model for user accounts."""
    name = CharField(
        max_length = 80
    )
    description = CharField(
        max_length = 240
    )
    servingQuantity = ForeignKey(
        ServingSize, 
        on_delete=CASCADE,
        related_name='servingQuantity_ServingSize',
        blank=True,
        null=True
    )
    skillLevel = ForeignKey(
        Difficulty, 
        on_delete=CASCADE,
        related_name='skillLevel_Difficulty',
        blank=True,
        null=True
    )
    prepmin = ForeignKey(
        PrepCookMin, 
        on_delete=CASCADE,
        related_name='prepmin_PrepCookMin',
        blank=True,
        null=True
    )
    prephour = ForeignKey(
        PrepCookHour, 
        on_delete=CASCADE,
        related_name='prephour_PrepCookHour',
        blank=True,
        null=True
    )
    cookmin = ForeignKey(
        PrepCookMin, 
        on_delete=CASCADE,
        related_name='cookmin_PrepCookMin',
        blank=True,
        null=True
    )
    cookhour = ForeignKey(
        PrepCookHour, 
        on_delete=CASCADE,
        related_name='cookhour_PrepCookHour',
        blank=True,
        null=True
    )
    author = ForeignKey(
        User, 
        on_delete=CASCADE,
        related_name='author_User',
        blank=True,
        null=True
    )
    # ingredient = ForeignKey(
    #     Ingredients,
    #     on_delete=CASCADE,
    #     blank=True, 
    #     related_name='ingredient_Ingredients'
    # )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})        
