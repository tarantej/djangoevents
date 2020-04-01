from django.db import models
from datetime import date


# Create your models here.
class EventsList(models.Model):
    event_name = models.CharField(max_length=200)
    event_date = models.DateField(auto_now=False, auto_now_add=False)
    event_location = models.CharField(max_length=200)
    event_desc = models.TextField(blank=True)
    featured_image = models.ImageField(upload_to='images/', blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name
