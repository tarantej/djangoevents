from django.urls import path
from . import views

urlpatterns = [
    path('', views.events_index, name='events_index'),
    # path('\add_events', views.add_events, name='add_events')
]