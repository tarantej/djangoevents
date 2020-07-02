from app.models import EventApp
from rest_framework import viewsets, permissions
from .serializers import AppSerializer


#   App Viewset

class AppViewSet(viewsets.ModelViewSet):
    queryset = EventApp.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = AppSerializer
