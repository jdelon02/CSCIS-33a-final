
from django.urls import path
from .views import recipe_view, user_view, ingredients_view
from .views.recipe_view import RecipeCreateView, RecipeUpdateView
from .views.ingredients_view import IngredientsCreateView


urlpatterns = [
    path("", recipe_view.Index.as_view(), name="index"),
    path('recipe/add/', RecipeCreateView.as_view(), name='recipe-add'),
    path('recipe/<int:pk>/', RecipeUpdateView.as_view(), name='recipe-update'),
    # path('author/<int:pk>/delete/', recipe_view.RecipeDeleteView.as_view(), name='recipe-delete'),
    path("login", user_view.login_view, name="login"),
    path("logout", user_view.logout_view, name="logout"),
    path("register", user_view.register, name="register"),
    # path("user/<int:pk>", user_view.UserDetailView.as_view(), name="user_detail"),
    path("bookmarks/<int:pk>", recipe_view.BookmarkListView.as_view(), name="bookmarks"),
    path("ingrdients", recipe_view.Index.as_view(), name="ingredients"),
    path('ingredients/add/', IngredientsCreateView.as_view(), name='ingr-add'),
    # API Routes
    # path("post/<int:post_id>",twitterpost_view.like_button, name='like'),
    # path("getpost/<int:post_id>",twitterpost_view.getPost, name='getPost'),
    # path("user/follow/<int:user_id>",user_view.followme, name='followme')

    
]