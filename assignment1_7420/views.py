from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Index Page')
    return render(request, 'pages/index.html')
    return render(request, 'events/index.html')