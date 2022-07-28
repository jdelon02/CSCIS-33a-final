"""This is a docstring which describes the module"""
import json
from django.db import IntegrityError
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.core.serializers import serialize
from django.core.paginator import Paginator
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from recipesite.models import *
from recipesite.forms import recipesform, ingredientlistsform, ingredientsform


paginationnum = 10


class Index(ListView):
    """This is a docstring which describes the module"""
    model = Recipes
    context_object_name = 'recipe_listview'
    template_name = 'recipesite/index.html'
    paginate_by = paginationnum
    
    # def get_context_data(self, *args, **kwargs):
    #     context = super(Index,
    #                     self).get_context_data(*args, **kwargs)
    #     current_user = self.request.user.id
    #     context['currentUser'] = current_user
        
    #     return context
    
    # def get_queryset(self):
    #     queryset = Recipes.objects.all().order_by('-id')
    #     return queryset
    

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
        # paginator = Paginator(self.get_queryset(), paginationnum)
        # context['paginator'] = paginator
        
        # page_number = self.request.GET.get('page')
        # context['page_number'] = page_number
        
        # page_obj = paginator.get_page(page_number)
        # context['page_obj'] = page_obj
        
        # page = self.request.GET.get('page')
        # context['page'] = page
        
        return context
    
    def get_queryset(self):
        current_user = self.request.user.id
        queryset = Recipes.objects.filter(user_id__in=current_user).distinct().order_by('-id')
        
        return queryset

            
            
# @csrf_exempt
# @login_required
# def like_button(request, post_id):
#     if request.method == "PUT":
#         data = json.loads(request.body)
#         userdata = User.objects.get(username=data['user'])
#         postdata = data['id']
#         postcheck=get_object_or_404(Twitterpost,pk=postdata)
#         if postcheck.likes.filter(id=userdata.id):
#             postcheck.likes.remove(userdata) #remove user from likes 
#             liked=False
#         else:
#             postcheck.likes.add(userdata)
#             liked=True
#         return JsonResponse({'likes':postcheck.total_likes, "likeclass":liked})
#     else:
#         return HttpResponse('CSRF token is being exempted here!')


@csrf_exempt
@login_required
def single_recipe(request):
    """This is a docstring which describes the module"""
    if request.method == "GET":
        template_name = 'recipesite/add.html'
        form = recipesform.RecipesForm()
        # bid_class = self.bid_class
        return render(request, template_name, {'form': form})

    elif request.method == "POST":
        form = recipesform(request.POST)
        current_userid = request.user.id
        current_user = User.objects.get(pk=current_userid)
        if form.is_valid():
            # new_post = Recipes()
            # new_post.body = form.data['body']
            # new_post.user_id = current_user
            # new_post.save()
            # form.save()
            # messages.add_message(request, messages.SUCCESS, 
                                # 'Post Added.')
            return HttpResponseRedirect(
                reverse_lazy('addpost'))
        else:
            # messages.add_message(
            #     request,
            #     messages.ERROR,
            #     'Post Not Added.')
            return render(request, template_name, {'form': form})


# @csrf_exempt
# def getPost(request, post_id):
#     if request.method == "GET":
#         print(post_id)
#         postcheck=Twitterpost.objects.get(pk=post_id)
#         userid = postcheck.user_id.id
#         # print(userid)
#         if postcheck:
#             jsonreply = postcheck.serialize()
#             return JsonResponse({"jsonreply":jsonreply, "id":userid})
#         else:
#             pass
#     elif request.method == "PUT":
#         data = json.loads(request.body)
#         print(data)
#         # postdata = User.objects.get(username=data['user'])
#         # postdata = data['id']
#         postcheck=get_object_or_404(Twitterpost,pk=post_id)
#         if postcheck:
#             postcheck.body = data
#             postcheck.save()
#             return JsonResponse(postcheck.serialize())
#     else:
#         return HttpResponse('CSRF token is being exempted here!')
