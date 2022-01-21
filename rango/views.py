from re import A
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/rango/about'>About</a>")

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")