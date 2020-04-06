from django.contrib import admin
from django.contrib.admin import ModelAdmin, actions
from .models import (NewsletterUser, Event, Video, Roster)


class AdminSite(admin.AdminSite):
    site_title = 'Harlem Dreams Basketball'


    

class EventAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("__unicode__","timestamp")
        
        # model = Event
        admin.site.register(Event)

class VideoAdmin(admin.ModelAdmin):
    admin.site.register(Video)

    # video = Video.object.all()

    # def delete():
    #     if len(video) > 1:
    #     print("success")
    #     video.delete()

class RosterAdmin(admin.ModelAdmin):

    class Meta:
        list_display = ("__unicode__",)


    admin.site.register(Roster)

    

