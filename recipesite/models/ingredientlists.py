"""Data models."""
from django.db import models
from django.contrib.auth.models import AbstractUser
# from .ingredients import Ingredients
# from .recipes import Recipes
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    IntegerField,
    TextField,
    ManyToManyField
)
 
class IngredientLists(Model):
    """Data model for user accounts."""
    recipe = ForeignKey(
        'Recipes',
        on_delete=CASCADE,
        blank=True,
        null=True
        
    )
    name = TextField(
        blank=True,
        null=True
    )
    unitId = IntegerField(
        blank=True,
        null=True
    )
    quantity = IntegerField(
        blank=True,
        null=True
    )
    description = TextField(
        blank=True,
        null=True
    )
    order = IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.id