"""This is a docstring which describes the module"""
import json
import re
from urllib.parse import urlparse
import requests
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy
from django.views import View
from recipesite.forms import scrapeform

def getIntegers(string):
    numbers = [int(x) for x in string.split() if x.isnumeric()]
    return numbers

def Index(request):
    """This is a docstring which describes the module"""
    if request.method == "POST":
        data = []
        
        # Just a quick check
        url = request.POST["url"]
        parsed_uri = urlparse(url)
        domain = parsed_uri.netloc
        path = parsed_uri.path
        print(path)
        data.append(parsed_uri)
        data.append(domain)
        data.append(path)
        id = getIntegers(path)
        data.append(id)
        
        # if food52, will need another check to pull out all integers
        
        # https://food52.com/recipes/88304-buttermilk-marinated-roast-chicken-from-samin-nosrat
        # http://feeds.feedburner.com/food52-TheAandMBlog
        
        return render(request, "recipesite/scrape_review.html", {'data':data})
    else:
        return render(request, "recipesite/scrapetemplate.html")