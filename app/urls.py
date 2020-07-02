from rest_framework import routers
from .api import AppViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()
router.register('api/app', AppViewSet, 'app')

urlpatterns = router.urls
