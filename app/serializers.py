from rest_framework import serializers
from app.models import EventApp, EventLocation, EventAttendee


#   EventApp Serializer

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventApp
        fields = '__all__'

# EventLocation Serializer


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventLocation
        fields = '__all__'

#   Event Attendee Serializer


class AttendeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventAttendee
        fields = '__all__'