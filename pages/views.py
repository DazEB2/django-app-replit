from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view():
    return HttpResponse("<h1>Hello There</h1>") # String of HTML Code