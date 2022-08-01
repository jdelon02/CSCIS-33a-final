from django.apps import AppConfig
from crispy_bootstrap5.bootstrap5 import FloatingField


class RecipesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'recipesite'
