"""This is a docstring which describes the module"""
import json
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from recipesite.models import *
from recipesite.forms import ingredientsform, recipesform
from recipesite.forms.recipesform import IngredientFormSet, RecipesForm


paginationnum = 10


class Index(ListView):
    """This is a docstring which describes the module"""
    model = Recipes
    context_object_name = 'recipe_listview'
    template_name = 'recipesite/index.html'
    paginate_by = paginationnum
    
class BookmarkListView(UserPassesTestMixin, ListView):
    model = Bookmarks
    context_object_name = 'recipes_listview'
    template_name = 'recipesite/bookmarks.html'
    paginate_by = paginationnum
    
    def test_func(self):
        test = self.request.user.id
        if test:
            return True
        else:
            return False

    def get_context_data(self, *args, **kwargs):
        context = super(BookmarkListView,
                        self).get_context_data(*args, **kwargs)
        current_user = self.request.user.id
        context['currentUser'] = current_user  
        return context
    
    def get_queryset(self):
        current_user = self.request.user.id
        queryset = Recipes.objects.filter(user_id__in=current_user).distinct().order_by('-id')
        return queryset


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipes
    # form_class = recipesform
    fields = [
        'name',
        'description',
        'servingQuantity',
        'skillLevel',
        'prepTimeHour',
        'prepTimeMin',
        'cookTimeHour',
        'cookTimeMin'
    ]
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeCreateView,
                        self).get_context_data(*args, **kwargs)
        current_user = self.request.user.id
        context['currentUser'] = current_user 
        context['formset'] = IngredientFormSet(queryset=Ingredients.objects.none()) 
        context['ingrient_form'] = ingredientsform
        
        return context
    
    # def get_queryset(self):
    #     current_user = self.request.user.id
    #     queryset = Recipes.objects.filter(user_id__in=current_user).distinct().order_by('-id')
    #     return queryset

class RecipeUpdateView(UpdateView):
    model = Recipes
    fields = ['name']
    def test_func(self):
        test = self.request.user.id
        if test:
            return True
        else:
            return False

    def get_context_data(self, *args, **kwargs):
        context = super(RecipeUpdateView,
                        self).get_context_data(*args, **kwargs)
        current_user = self.request.user.id
        context['currentUser'] = current_user  
        return context

# class RecipeDeleteView(DeleteView):
#     model = Recipes
#     success_url = reverse_lazy('recipe-list')
    
    
# def single_recipe(request):
#     """This is a docstring which describes the module"""
#     if request.method == "GET":
#         template_name = 'recipesite/add.html'
#         form = recipesform.RecipesForm()
#         ingredientformset = IngredientFormSet
#         # bid_class = self.bid_class
#         return render(request, template_name, {'form': form, 'ingredientformset': ingredientformset})

#     elif request.method == "POST":
#         form = recipesform(request.POST)
#         current_userid = request.user.id
#         current_user = User.objects.get(pk=current_userid)
#         if form.is_valid():
#             # new_post = Recipes()
#             # new_post.body = form.data['body']
#             # new_post.user_id = current_user
#             # new_post.save()
#             # form.save()
#             # messages.add_message(request, messages.SUCCESS, 
#                                 # 'Post Added.')
#             return HttpResponseRedirect(
#                 reverse_lazy('addpost'))
#         else:
#             # messages.add_message(
#             #     request,
#             #     messages.ERROR,
#             #     'Post Not Added.')
#             return render(request, template_name, {'form': form})
