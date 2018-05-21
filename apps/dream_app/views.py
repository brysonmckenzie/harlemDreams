from django.shortcuts import render, redirect, HttpResponse



def index(request):
    
    return render(request, 'dream_app/index.html')

def about(request):
    
    return render(request, 'dream_app/about.html')

def shop(request):

    return render(request, 'dream_app/shop.html')

def events(request):
    
    return render(request, 'dream_app/events.html')

def newsletter(request):
    
    return render(request, 'dream_app/newsletter.html')
    
def players(request):
    
    return render(request, 'dream_app/players.html')
