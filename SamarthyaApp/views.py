# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
import socket
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from .models import payment
from django.contrib.auth.forms import AuthenticationForm




def Index(request):
    return render(request, 'index.html')


def Gallery(request):
    return render(request, 'gallery.html')



def profile(request, pk):
    if request.user.is_authenticated:
        profiledb = User.objects.get(id=pk)
        pay = payment.objects.get(id=pk)
        # for i in payment:
        print(pay.text)
        return render(request, 'profile.html', {'pdb':profiledb,'p':pay})


def about(request):
    return render(request, 'about.html')

def instant_speech(request):
    return render(request,'instant_speech.html')

def word_blocks(request):
    return render(request,'word_blocks.html')

def codebuster(request):
    return render(request,'codebuster.html')

def math_buzz(request):
    return render(request,'math_buzz.html')
def jam(request):
    return render(request,'jam.html')
