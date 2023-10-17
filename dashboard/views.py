from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("THIS IS THE INDEX PAGE")

def staff(request):
    return HttpResponse("THIS IS THE STAFF PAGE")
