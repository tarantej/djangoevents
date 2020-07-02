from rest_framework import serializers
from app.models import EventApp


#   EventApp Serializer

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventApp
        fields = '__all__'
