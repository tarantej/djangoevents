from app.models import EventApp, EventLocation, EventAttendee
from rest_framework import viewsets, permissions
from .serializers import AppSerializer, LocationSerializer, AttendeeSerializer


#   App ViewSet

class AppViewSet(viewsets.ModelViewSet):
    queryset = EventApp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSerializer


#   Location ViewSet

class LocationViewSet(viewsets.ModelViewSet):
    queryset = EventLocation.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LocationSerializer


#   Attendee ViewSet

class AttendeeViewSet(viewsets.ModelViewSet):
    queryset = EventAttendee.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AttendeeSerializer
