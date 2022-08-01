"""This is a docstring which describes the module"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from .user import User
# from .food import Food
from .difficulty import Difficulty
# from .quantitywhole import QuantityWhole
# from .quantityfraction import QuantityFraction
from .servingsize import ServingSize
from .units import Units
from .prepcookmin import PrepCookMin
from .prepcookhour import PrepCookHour
from .ingredients import Ingredients
from .recipes import Recipes
from .bookmarks import Bookmarks
from .userfollowing import UserFollowing

# from . import *
