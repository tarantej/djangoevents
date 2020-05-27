from django.shortcuts import render
from django.template import context

from .models import EventsList


# Create your views here.
def events_index(request):
    events = EventsList.objects.all()

    test = {'name': 'Taran'}

    event_context = {
        'Events': events
    }

    return render(request, 'events/index.html', event_context)


# def add_events(request):
#     return render(request, 'events/add_event.html')


def event(request, event_name):
    return render(request, 'events/event.html', event_context)
