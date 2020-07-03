from __future__ import unicode_literals
from django.db import models
# from embed_video.fields import EmbedVideoField





class Event(models.Model):
    opponent = models.CharField(max_length=30)
    date = models.DateField(auto_now=False, auto_now_add=False)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    description = models.TextField(max_length=200)
    location = models.CharField(max_length=50)
    image = models.ImageField(upload_to='events', blank=True)
    hd_event_logo = models.ImageField(upload_to='events/hd_logo_main', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return(self.opponent + " vs The Harlem Dreams")


class Photo(models.Model):
    name =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='carousel')
    description =  models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return(self.name + " - " + self.description)


class Notice(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    message = models.TextField(max_length=600, blank=True, null=True)
    active = models.BooleanField(default=True)
    color = models.CharField(max_length=256, choices=[('green', 'green'), ('red', 'red'), ('blue', 'blue')], null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        if active == true:
            return(self.name + "(active)")
        else:
            return(self.name + "(inactive)")
        

    


class Player(models.Model):
    image = models.ImageField(upload_to='team')
    number = models.CharField(max_length=3, blank=True, null=True)
    show_number = models.BooleanField(default=True)
    no_number_sign = models.BooleanField(default=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    bio = models.TextField(max_length=1000, blank=True, null=True)
    position = models.CharField(max_length=20, blank=True, null=True)
    quote = models.TextField(max_length=1000, blank=True, null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return(self.name)


class SiteLink(models.Model):
    facebook = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    homepage_phone = models.CharField(max_length=15, blank=True, null=True) # validators should be a list
    contact_page_phone = models.CharField(max_length=15, blank=True, null=True) # validators should be a list
    contact_email = models.CharField(max_length=40, blank=True,null=True) # validators should be a list
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)



    def __str__(self):
        return("links configurations (limit to one record)")