from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Index Page')
    return render(request, 'pages/index.html')


def events_index(request):
    return render(request, 'events/index.html')


def add_events(request):
    return render(request, 'events/add_event.html')


def about(request):
    return render(request, 'pages/about.html')
