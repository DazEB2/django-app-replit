from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, dazeb")

def page(request):
    return HttpResponse("new page")