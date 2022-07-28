"""Data models."""
from django.db import models
from .user import User
from .ingredientlists import IngredientLists
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
    userId = ForeignKey(
        User, 
        on_delete=CASCADE,
        related_name='likes'
    )
    ingredients_list = ManyToManyField(
        IngredientLists, 
        blank=True
    )
    

    def __str__(self):
        return self.name
        
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