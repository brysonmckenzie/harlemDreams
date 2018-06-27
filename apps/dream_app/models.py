from __future__ import unicode_literals
from django.db import models

class NewsletterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Event(models.Model):
    opponent = models.CharField(max_length=30)
    date = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    time = models.CharField(max_length=30)
    desc = models.TextField(max_length=30)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)


class Message(models.Model):
    message = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)