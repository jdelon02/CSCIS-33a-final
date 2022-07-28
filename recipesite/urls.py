
from django.urls import path
from .views import recipe_view, user_view


urlpatterns = [
    path("", recipe_view.Index.as_view(), name="index"),
    path("add", recipe_view.single_recipe, name="addpost"),
    path("login", user_view.login_view, name="login"),
    path("logout", user_view.logout_view, name="logout"),
    path("register", user_view.register, name="register"),
    # path("user/<int:pk>", user_view.UserDetailView.as_view(), name="user_detail"),
    path("bookmarks/<int:pk>", recipe_view.BookmarkListView.as_view(), name="bookmarks"),
    
    # API Routes
    # path("post/<int:post_id>",twitterpost_view.like_button, name='like'),
    # path("getpost/<int:post_id>",twitterpost_view.getPost, name='getPost'),
    # path("user/follow/<int:user_id>",user_view.followme, name='followme')

    
]