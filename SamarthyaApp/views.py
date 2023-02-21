# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
import socket
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from .models import payments
from django.contrib.auth.forms import AuthenticationForm




def Index(request):
    return render(request, 'index.html')


def Gallery(request):
    return render(request, 'gallery.html')



def profile(request, pk):
    if request.user.is_authenticated:
        profiledb = User.objects.get(id=pk)
        pay = payments.objects.all()
        print(profiledb)
        
        return render(request, 'profile.html', {'pdb':profiledb,'p':pay})


def about(request):
    return render(request, 'about.html')
