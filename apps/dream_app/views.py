from django.shortcuts import render, redirect, HttpResponse

from models import Event


from django.core.mail import send_mail

from django.conf import settings


def index(request):
    event_message = 'Join us, check Events for more information'

    context = {
        'message' : event_message
    }

    return render(request, 'dream_app/index.html', context)

def jobs(request):
    
    return render(request, 'dream_app/job-openings.html')

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
    
    no_event_message = "Sorry, no events have been scheduled as of yet"

    context = {
        'events': Event.objects.all(),
        'no_event': no_event_message
    }

    print 

    return render(request, 'dream_app/events.html', context)

def newsletter(request):
    
    return render(request, 'dream_app/newsletter.html')
    
def players(request):
    
    return render(request, 'dream_app/players.html')

def contact(request):
    
    return render(request, 'dream_app/contact.html')

def process_contact(request):
    
    if request.method == 'POST': 

        server_name = request.POST['client_name']
        server_subject = request.POST['client_subject']
        server_email = request.POST['client_email']
        server_message = request.POST['client_message']
        from_email = settings.EMAIL_HOST_USER

            # Message.objects.create(
            #         name = server_name,
            #         subject = server_subject,
            #         email = server_email,
            #         message = server_message
            #     )

        

        # send_mail(server_subject, 
        #     server_message 
        #     from_email, 
        #     [to_email], fail_silently=true)

        send_mail(server_subject, server_message, from_email, [server_email])

        print '***** New Contact Info has Arrived *****'

        return redirect('/')
