from django.shortcuts import render


# Create your views here.
def events_index(request):
    return render(request, 'events/index.html')


def add_events(request):
    return render(request, 'events/add_event.html')
