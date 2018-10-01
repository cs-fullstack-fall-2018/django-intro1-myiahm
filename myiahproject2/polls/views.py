from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    return HttpResponse('"This is a bad request. Use one of the other routes"')
def language(request):
    return HttpResponse("My favorite language is Python :) .")
def system(request):
    return HttpResponse("My favorit system is Linux")
def IDE(request):
    return HttpResponse("My favorite IDE is IntelliJ")