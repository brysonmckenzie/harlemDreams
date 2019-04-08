from django.contrib import admin
from django.contrib.admin import ModelAdmin, actions
from .models import (NewsletterUser, Event)


class AdminSite(admin.AdminSite):
    site_title = 'Harlem Dreams Basketball'


    

class EventAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("__unicode__","timestamp")
        
        # model = Event
        admin.site.register(Event)