from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    #return HttpResponse("<h1>Hello There</h1>") # String of HTML Code
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>") # String of HTML Code

def about_view(request, *args, **kwargs):
    return HttpResponse("<h1>About Page</h1>") # String of HTML Code

def blog_view(request, *args, **kwargs):
    return HttpResponse("<h1>Blog Page</h1>") # String of HTML Code

def socials_view(request, *args, **kwargs):
    return HttpResponse("<h1>Socials Page</h1>") # String of HTML Code    