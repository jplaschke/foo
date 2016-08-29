from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
