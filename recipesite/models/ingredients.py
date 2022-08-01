"""Data models."""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    IntegerField,
    TextField,
    CharField
)
from . import Units
 
class Ingredients(Model):
    UNITSTATUS = Choices(
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
    unitId = CharField(
        max_length = 10,
        choices=UNITSTATUS        
    )
    quantitywhole = CharField(
        max_length=2
    )
    quantityfraction = CharField(
        max_length = 8,
        choices=QUANTS        
    )
    description = CharField(
        max_length=100,
        blank=True,
        null=True
    )
    order = IntegerField(
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name