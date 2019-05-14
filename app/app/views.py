from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Welcome to Index")

def handle_custom_string(request, some_string):
    return HttpResponse(some_string)

def another_url(request):
    return HttpResponse("This is another!")