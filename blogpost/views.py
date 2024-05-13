from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def app_homeview(request):
    return HttpResponse("hello world")

def blogpost(request):
    return HttpResponse("blogpost/")

