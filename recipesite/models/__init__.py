"""This is a docstring which describes the module"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .user import User
from .ingredients import Ingredients
from .ingredientlists import IngredientLists
from .bookmarks import Bookmarks
from .recipes import Recipes

# from . import *