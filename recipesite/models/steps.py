"""Data models."""
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey,
    CharField,
)

# TODO: Description Field to model, recipe.
class Steps(Model):

    step = CharField(
        max_length = 240
    )
    recipe = ForeignKey(
        'Recipes',
        on_delete=CASCADE,
        related_name='recipe_Steps',
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.step
        # return str(self.name)    