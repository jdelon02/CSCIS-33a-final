"""This is a docstring which describes the module"""
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from django.forms import IntegerField, ModelForm
from django.db.models import (
    Model,
    CASCADE,
    CharField
)


class Units(Model):
    
    # UNITSTATUS = Choices(
    #     ('unit', ('Unit')),
    #     ('cup', ('Cup')),
    #     ('tablespoon', ('Tablespoon')),
    #     ('teaspoon', _('Teaspoon')),
    #     ('pint', _('Pint')),
    #     ('quart', _('Quart')),
    #     ('ounce', _('Ounce')),
    #     ('dozen', _('Dozen')),
    #     ('can', _('Can')),
    #     ('bunch', _('Bunch')),
    #     ('whole', _('Whole')),
    # )

    unit = CharField(
        primary_key=True,
        max_length = 10,
        # choices = UNITSTATUS,
        # default = UNITSTATUS.unit
    )
    