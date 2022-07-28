"""Data models."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .ingredients import Ingredients
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
    ingredient = ForeignKey(
        Ingredients, 
        on_delete=CASCADE,
        related_name='ingr_name'
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