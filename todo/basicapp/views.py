from django.shortcuts import render, redirect
from basicapp.models import *

def home(request):
    
    return render(request, 'home.html')
