from django.contrib import admin
from django.contrib.admin import ModelAdmin, actions
from .models import (Event, Player, Photo, Notice, SiteLink)


class AdminSite(admin.AdminSite):
    site_title = ('Harlem Dreams Basketball'
)

    

class EventAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("__unicode__","timestamp")
        
        # model = Event
        admin.site.register(Event)

# class VideoAdmin(admin.ModelAdmin):
#     admin.site.register(Video)

    # video = Video.object.all()

    # def delete():
    #     if len(video) > 1:
    #     print("success")
    #     video.delete()

class PlayerAdmin(admin.ModelAdmin):

    

    admin.site.register(Player)

class PhotoAdmin(admin.ModelAdmin):

    admin.site.register(Photo)
    
class Notice(admin.ModelAdmin):
    admin.site.register(Notice)

    # def has_add_permision(self, request):
    #     base_add_persmission = super(SettingAdmin, self).has_add_permission(request)
    #     if base_add_persmission:
    #         #if there's already an entry, do not allow adding
    #         count == Notice.object.all().count()
    #         if count == 0:
    #             return True
    #         return False

    def has_add_permission(self, *args, **kwargs):
        return not Notice.objects.exists()

class SiteLink(admin.ModelAdmin):
    admin.site.register(SiteLink)

    def has_add_permission(self, *args, **kwargs):
        return False if self.SiteLink.objects.count() > 0 else super().has_add_permission(request)