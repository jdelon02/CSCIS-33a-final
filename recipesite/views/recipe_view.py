"""This is a docstring which describes the module"""
import json
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.forms import modelformset_factory
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
from recipesite.forms.recipesform import RecipesForm, IngredientFormSet


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


# class RecipeCreateView(LoginRequiredMixin, CreateView):
class RecipeCreateView(CreateView):
    model = Recipes
    form_class = RecipesForm
    template_name = 'recipesite/recipes_form.html'
    
    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        formset = IngredientFormSet()
        return self.render_to_response(
                self.get_context_data(form=form,
                        formset=formset,
                                )
                        )

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        # formset = IngredientFormSet(self.request.POST)
        formset = IngredientFormSet(self.request.POST, instance=form.instance)
        if form.is_valid() and formset.is_valid():
            return self.form_valid(form, formset)
        else:
            return self.form_invalid(form, formset)

    def form_valid(self, form, formset):
        print(form.instance)
        recipe = form.save(commit=False)
        
        recipe.author = self.request.user
        recipe.servingQuantity = ServingSize.objects.create(serving=form.data['servingQuantity'])
        recipe.skillLevel = Difficulty.objects.create(level=form.data['skillLevel'])
        recipe.prepmin = PrepCookMin.objects.create(timeMin=form.data['prepmin'])
        recipe.prephour = PrepCookHour.objects.create(timeHour=form.data['prephour'])
        recipe.cookmin = PrepCookMin.objects.create(timeMin=form.data['cookmin'])
        recipe.cookhour = PrepCookHour.objects.create(timeHour=form.data['cookhour'])
        
        recipe.save()
        ingredientlist = formset.save(commit=False)
        for ingr in ingredientlist:
            ingr.instance = self.object
            ingr.save()
        return HttpResponseRedirect(
                reverse_lazy('recipe-add'))
        
    # def form_valid(self, form, education_formset):
    #     # with transaction.atomic():
    #     form.instance.employee.user = self.request.user
    #     self.object = form.save()
    #     # Now we process the education formset
    #     educations = education_formset.save(commit=False)
    #     for education in educations:
    #         education.instance = self.object
    #         education.save()
    #         # If you had more formsets, you would accept additional arguments and
    #         # process them as with the one above.
    #     # Don't call the super() method here - you will end up saving the form twice. Instead handle the redirect yourself.
    #     return HttpResponseRedirect(self.get_success_url())

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
