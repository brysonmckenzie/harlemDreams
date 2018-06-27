from django.contrib import admin

from .models import NewsletterUser, Event

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewsletterUser, NewsletterAdmin)


class EventAdmin(admin.ModelAdmin):
    class Meta:
        list_display = ("__unicode__","timestamp", "opponent")
        # model = Event
        admin.site.register(Event)