"""Data models."""
from django.db import models
from django.urls import reverse
from .user import User
# from .ingredientlists import IngredientLists
# from .ingredients import Ingredients
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    IntegerField,
    TextField,
    ManyToManyField
) 

# TODO: Description Field to model, recipe.
class Recipes(Model):
    """Data model for user accounts."""
    name = TextField(
        blank=True,
        null=True
    )
    description = TextField(
        blank=True,
        null=True
    )
    servingQuantity = IntegerField(
        blank=True,
        null=True
    )
    skillLevel = IntegerField(
        blank=True,
        null=True
    )
    prepTimeHour = IntegerField(
        blank=True,
        null=True
    )
    prepTimeMin = IntegerField(
        blank=True,
        null=True
    )
    cookTimeHour = IntegerField(
        blank=True,
        null=True
    )
    cookTimeMin = IntegerField(
        blank=True,
        null=True
    )
    author = ForeignKey(
        'User', 
        on_delete=CASCADE,
        related_name='authors',
        blank=True,
        null=True
    )
    ingredient = ManyToManyField(
        'Ingredients'
        # through='IngredientLists'
    )
    

    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self):
        return reverse('recipe-detail', kwargs={'pk': self.pk})    
    # def from_form(self, form):
    #     self.id = form.id.data
    #     self.name = form.name.data
    #     self.description = form.description.data
    #     self.filename = form.filename.data
    #     self.servingQuantity = form.servingQuantity.data
    #     self.skillLevel = form.skillLevel.data
    #     self.prepTimeHour = form.prepTimeHour.data
    #     self.prepTimeMin = form.prepTimeMin.data
    #     self.cookTimeHour = form.cookTimeHour.data
    #     self.cookTimeMin = form.cookTimeMin.data
    #     self.userId = form.userId.data
    
