from rest_framework import routers
from .api import AppViewSet, LocationViewSet, AttendeeViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('events-list', AppViewSet, 'events')
router.register('location-list', LocationViewSet, 'location')
router.register('attendee-list', AttendeeViewSet, 'attendee')

urlpatterns = router.urls
