from django.contrib import admin

# Register your models here.

from .models import EventsList, Location

admin.site.register(EventsList)
admin.site.register(Location)
