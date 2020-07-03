from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^about$', views.about),
    url(r'^shop$', views.shop),
    url(r'^events$', views.events),
    url(r'^team$', views.team),
    url(r'^contact-page$', views.contact),
    url(r'^process$', views.process_contact),
    url(r'^sponsors$', views.sponsors),
    url(r'^founders$', views.founder),
    url(r'^dreamsmedia$', views.media),
]