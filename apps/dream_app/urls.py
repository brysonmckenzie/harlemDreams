from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^shop$', views.shop),
    url(r'^newsletter$', views.newsletter),
    url(r'^events$', views.events),
    url(r'^players$', views.players),
    url(r'^contact-page$', views.contact),
    url(r'^job-openings$', views.jobs),
    url(r'^job_process$', views.job_process),
    url(r'^process$', views.process_contact),
]