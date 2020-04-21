from django.shortcuts import render


# Create your views here.
from events.models import EventsList


def events_index(request):

    events = EventsList.objects.all()

    context = {
        'Event': events
    }

    return render(request, 'events/index.html', context)


# def add_events(request):
#     return render(request, 'events/add_event.html')
