"""Data models."""
from django.db import models
from django.db.models import (
    Model,
    TextField
)
 
class Ingredients(Model):
    """Data model for user accounts."""
    name = TextField(
        blank=True,
        null=True
    )