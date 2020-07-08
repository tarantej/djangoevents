from django.db import models


class EventApp(models.Model):
    eventName = models.CharField(max_length=200)
    eventDate = models.DateField(auto_now=False, auto_now_add=False)
    location = models.CharField(max_length=200)
    eventDescription = models.TextField(blank=True)


class EventLocation(models.Model):
    location = models.CharField(max_length=100)


class EventAttendee(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    attEmail = models.EmailField()
