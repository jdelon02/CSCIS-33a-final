"""This is a docstring which describes the module"""
from django.db import models
from .user import User
from .recipes import Recipes
from django.db.models import (
    Model,
    CASCADE,
    ForeignKey
)

class Bookmarks(Model):
    user = ForeignKey(
        User, 
        on_delete=CASCADE
    )
    recipes = ForeignKey(
        Recipes, 
        on_delete=CASCADE,
        related_name='recipes'
    )
    
    
    def __str__(self):
        return self.id