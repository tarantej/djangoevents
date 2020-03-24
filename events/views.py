from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def events_index(request):
    #   return HttpResponse('Events index Page')
    return render(request, 'events/index.html')
