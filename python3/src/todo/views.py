from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    # return render(request, "music_app/index.html")
    return HttpResponse("HelloWorld!")
