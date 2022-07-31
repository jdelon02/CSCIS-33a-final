"""Data models."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    IntegerField,
    TextField,
    CharField
)
from . import Units, QuantityWhole, QuantityFraction
 
class Ingredients(Model):
    
    """Data model for user accounts."""
    recipe = ForeignKey(
        'Recipes',
        on_delete=CASCADE,
        related_name='recipe_Recipes',
        blank=True,
        null=True
    )
    name = CharField(
        blank=False,
        null=True,
        max_length=75
    )
    unitId = ForeignKey(
        Units,
        on_delete=CASCADE,
        related_name='unitId_Units',
        blank=True,
        null=True
    )
    quantitywhole = ForeignKey(
        QuantityWhole,
        on_delete=CASCADE,
        related_name='quantitywhole_QuantityWhole',
        blank=True,
        null=True
    )
    quantityfraction = ForeignKey(
        QuantityFraction,
        on_delete=CASCADE,
        related_name='quantityfraction_QuantityFraction',
        blank=True,
        null=True
    )
    description = CharField(
        max_length=210,
        blank=True,
        null=True
    )
    order = IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.id