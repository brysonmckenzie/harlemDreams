from django.shortcuts import render, redirect, HttpResponse



def index(request):
    
    return render(request, 'dream_app/index.html')

def page2(request):

    return render(request, 'dream_app/index2.html')
