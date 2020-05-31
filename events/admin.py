from django.contrib import admin

# Register your models here.

from .models import (
    EventsList,
    Location,
    Attendee,
    Delegates,
    Company,
)


#   Change display / view of Events Listings

class EventsAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'location', 'event_date', 'is_published')

    #   Linking Event Name so that we can edit by clicking on it

    list_display_links = ('id', 'event_name')

    # Filter Events according Event Location.
    # If we are filtering only one value then it should have a comma (,
    # ) at the end of field name or it will give an error

    list_filter = ('location__name',)

    #   Publish / Un-publish events

    list_editable = ('is_published',)

    #   Search Events

    search_fields = ('event_name', 'location__name')

    #   Number of Events to display per page

    list_per_page = 20


class DelegateAdmin(admin.ModelAdmin):
    # verbose_name_plural = 'Delegate'
    pass

    # Show Delegate Details

    list_display = ('delegate_name', 'company_name', 'position', 'event_registered_for')

    # Show 20 Delegates per page

    list_per_page = 20

class AttendeeAdmin(admin.ModelAdmin):

    #Show Attendee Details

    list_display = ('first_name', 'last_name', 'phone', 'email')

    #Show 20 Attendees per page

    list_per_page = 20


admin.site.register(EventsList, EventsAdmin)
admin.site.register(Location)
admin.site.register(Company)
admin.site.register(Attendee, AttendeeAdmin)
admin.site.register(Delegates, DelegateAdmin)
