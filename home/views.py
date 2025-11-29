from django.shortcuts import HttpResponse ,render

# Create your views here.

def index(request):
    return HttpResponse("Hello, Worls! Dávisson Tiago")

def sobre(request):
    return HttpResponse("Sobre o Sistema!")
