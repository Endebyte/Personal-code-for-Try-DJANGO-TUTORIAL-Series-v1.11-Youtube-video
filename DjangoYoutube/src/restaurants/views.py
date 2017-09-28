from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.
#function based view

#     #return render(request, "home.html",{})#response

def home(request):
    num = None
    some_list = [
        random.randint(0, 1000000),
        random.randint(0, 1000000),
        random.randint(0, 1000000)
        ]
    condition_bool_item = False
    if condition_bool_item:
        num = random.randint(0, 999999999)
    context = {
                "num": num,
                "some_list": some_list
    }
    return render(request, "base.html", context) #home.html
