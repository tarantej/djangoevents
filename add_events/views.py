from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def add_events(request):
    return HttpResponse('Add Events Page')
