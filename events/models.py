"""
   Documentation for the models
"""

from django.db import models
from datetime import date


# Create your models here.

#   Events Model


class EventsList(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    location = models.ForeignKey('Location', related_name='events', on_delete=models.CASCADE)
    event_desc = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='images/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name


#   Attendee Model

class Attendee(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


#   Delegate Model

class Delegates(models.Model):
    delegate_name = models.CharField(max_length=250)
    company_name = models.ForeignKey('Company', related_name='delegates', on_delete=models.CASCADE)
    position = models.CharField(max_length=250)
    event_registered_for = models.ForeignKey('EventsList', related_name='delegates', on_delete=models.CASCADE)

    def __str__(self):
        return self.delegate_name

    class Meta:
        verbose_name_plural = 'Delegate'

#   Location Model

class Location(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

#   Company / Organization Model

class Company(models.Model):
        name = models.CharField(max_length=250)

        def __str__(self):
            return self.name

    # Notifications
    # Messages
    # Custom Image Model
    # Recurring Event Field
    # Blog
    # Booking
    # Sponsors
    # Organizations
    # Terms and Conditions / Custom Event Requirements

