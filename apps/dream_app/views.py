from django.shortcuts import render, redirect, HttpResponse

from .models import Event, Player, Photo, SiteLink, Notice

from django.core.mail import send_mail

from django.conf import settings


def index(request):
    event_message = 'Join us, check Events for more information'
    home_notice = Notice.objects.all()
    links = SiteLink.objects.all()
    


       

    context = {
        'message' : event_message,
        'photos' : Photo.objects.all(),
        'notice' : home_notice,
          }
       

    return render(request, 'dream_app/index.html', context)


def job_process(request):

    server_name = request.POST['client_name']
    server_position = request.POST['client_position']
    server_address = request.POST['client_address']
    server_address2 = request.POST['client_address2']
    server_city = request.POST['client_city']
    server_state = request.POST['client_state']
    server_zip = request.POST['client_zip']
    server_age = request.POST['client_age']
    server_email = request.POST['client email']
    server_q1 = request.POST['client_q1']
    server_q2 = request.POST['client_q2']
    server_q3 = request.POST['client_q3']

    return redirect('/')


def about(request):

    return render(request, 'dream_app/about.html')


def shop(request):

    return render(request, 'dream_app/shop.html')


def events(request):

    no_event_message = "Updates are coming soon. Stay tuned!"

    context = {
        'events': Event.objects.all(),
        'no_event': no_event_message
    }

    return render(request, 'dream_app/events.html', context)


def team(request):

    active_players = Player.objects.get()
    hdp = Player.objects.all()

    

    for index in hdp:
        print(index.active)
        if index.active == True:
            active_players = True
        
    print(active_players)


    context = {
        'players' : Player.objects.all(),
        'active' : active_players,
    }

    # print(hdp)



    return render(request, 'dream_app/team.html', context)


def contact(request):
    links = SiteLink.objects.all()
    contact_phone = links.contact_page_phone
    contact_email = links.contact_email
    all_links = links.contact_phone.lengthls > 1
    
    context = {
        'phone': contact_phone,
        'email': contact_email,
    }


    if links.contact_phone.lenght > 1:
        for index in contact_phone:
            print (index)

    return render(request, 'dream_app/contact.html', context)


def sponsors(request):

    return render(request, 'dream_app/sponsors.html')


def founder(request):

    return render(request, 'dream_app/founders.html')


def media(request):

    return render(request, 'dream_app/media.html')


def process_contact(request):

    if request.method == 'POST':

        server_name = request.POST['client_name']
        server_subject = request.POST['client_subject']
        server_email = request.POST['client_email']
        server_message = request.POST['client_message']
        from_email = settings.EMAIL_HOST_USER



        send_mail(server_subject, server_message, server_email, [
                  'contact@harlemdreams.net'], fail_silently=False,)

        print('***** New Contact Info has Arrived *****')
        print(""" Success! Email Worked """)

        return redirect('/')

def notice(request):
    
    return redirect('/')


