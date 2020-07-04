from django.urls import path
from . import views

urlpatterns = [
    path('', views.react_index, name='react_index'),
]
