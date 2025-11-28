from django.shortcuts import render

# Create your views here.

def index(request):
    return HttResponse("Hello, Worls! Dávisson Tiago")

def sobre(request):
    return HttResponse("Sobre o Sistema!")
