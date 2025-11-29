from django.shortcuts import HttpResponse ,render

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello, Worlds!<h1> <br> <hr> <h2>Dávisson Tiago<h2>")

def sobre(request):
    return HttpResponse("<h1>Sobre o Sistema!<h1>")
