


from django.contrib import admin
from django.contrib.admin import ModelAdmin, actions
from .models import (NewsletterUser)

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewsletterUser, NewsletterAdmin)
