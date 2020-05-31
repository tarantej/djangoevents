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
    location = models.ForeignKey('Location', related_name='events', on_delete=models.CASCADE, blank=True)
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
    company_name = models.CharField(max_length=250)
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
        company_id = models.AutoField(primary_key=True)
        company_name = models.CharField(max_length=250)
        company_name_id = models.CharField(max_length=20, blank=True)

        def __str__(self):
            return self.company_name

#   Blog
class Blog(models.Model):
    post_title =  models.CharField(max_length=250)
    post_date = models.DateField()
    post_desc = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='images/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.post_title


#   Sponsors

class Sponsors(models.Model):
    brand_name = models.CharField(max_length=250)
    brand_type = models.CharField(max_length=250)
    parent_company = models.CharField(max_length=250)
    for_event  = models.CharField(max_length=250)


    # Notifications
    # Messages
    # Custom Image Model
    # Recurring Event Field
    # Booking
    # Terms and Conditions / Custom Event Requirements

