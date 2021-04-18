from django.shortcuts import render
from django.http import HttpResponse


def page_home(request):
    return render(request, 'pages/home.html')

def page_about(request):
    return render(request, 'pages/about.html')
