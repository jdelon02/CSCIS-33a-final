
from django.urls import path
from .views import recipe_view, user_view, ingredients_view
from .views.recipe_view import RecipeCreateView, RecipeUpdateView, BookmarkListView, RecipeDetailView
from .views.ingredients_view import IngredientsCreateView
from .views.user_view import UserDetailView


urlpatterns = [
    path("recipe", recipe_view.Index.as_view(), name="index"),
    path('recipe/add/', recipe_view.RecipeCreateView.as_view(), name='recipeadd'),
    path('recipe/<int:pk>', recipe_view.RecipeDetailView.as_view(), name='recipedetail'),
    path('recipe/<int:pk>/edit', recipe_view.RecipeUpdateView.as_view(), name='recipeupdate'),
    path('recipe/', recipe_view.Index.as_view(), name='recipesearch'),
    path("bookmarks", recipe_view.BookmarkListView.as_view(), name="bookmarks"),
    # path('author/<int:pk>/delete/', recipe_view.RecipeDeleteView.as_view(), name='recipe-delete'),
    
    path("login", user_view.login_view, name="login"),
    path("logout", user_view.logout_view, name="logout"),
    path("register", user_view.register, name="register"),
    path("user/<int:pk>", user_view.UserDetailView.as_view(), name="user_detail"),
    # path("ingredients", ingredients_view.Index.as_view(), name="ingredients"),
    # path('ingredients/add/', IngredientsCreateView.as_view(), name='ingr-add'),
    
    # API Routes
    path("api/recipe/<int:recipe_id>",recipe_view.RecipeDetailView.like_button, name='like'),
    path("api/bookmark/<int:recipe_id>",recipe_view.BookmarkListView.save_button, name='save'),
    # path("api/getrecipe/<int:recipe_id>",recipe_view.RecipeDetailView.getRecipe, name='getRecipe'),
    # path("api/user/follow/<int:user_id>",user_view.followme, name='followme')

    
]