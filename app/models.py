from django.db import models


class EventApp(models.Model):
    eventName = models.CharField(max_length=200)
    eventDate = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    eventDescription = models.TextField(blank=True)
