from __future__ import unicode_literals
from django.db import models

class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

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

class Video(models.Model):
    video_link_name = models.CharField(max_length=20)
    link = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return(self.video_link_name)

class Photo(models.Model):
    name =  models.CharField(max_length=30)
    image = models.ImageField(upload_to='carousel')
    description =  models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return(self.name + " - " + self.description)
    





class Player(models.Model):
    image = models.ImageField(upload_to='team')
    number = models.CharField(max_length=3, blank=True)
    show_number = models.BooleanField(default=True)
    no_number_sign = models.BooleanField(default=True)
    name = models.CharField(max_length=50, blank=True)
    bio = models.TextField(max_length=1000, blank=True)
    position = models.CharField(max_length=20, blank=True)
    quote = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    def __str__(self):
        return(self.name)