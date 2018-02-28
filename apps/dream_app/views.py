from django.shortcuts import render, redirect, HttpResponse



def index(request):

    return render(request, 'dream_app/index.html')
