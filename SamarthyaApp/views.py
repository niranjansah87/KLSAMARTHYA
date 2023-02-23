# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
from django.contrib import messages
from django.conf import settings
import socket
from django.http import HttpResponseServerError
from django.contrib.auth.models import User
from .models import bool_model
from django.contrib.auth.forms import AuthenticationForm




def Index(request):
    return render(request, 'index.html')


def Gallery(request):
    return render(request, 'gallery.html')

def Profile(request,pk):
    if request.user.is_authenticated:
        user=User.objects.get(id=pk)
        context={
            'pdb':user,
        }
        return render(request,"profile.html",context)
    else:
        return redirect("login")



def about(request):
    return render(request, 'about.html')

def instantspeech(request):
    return render(request,'instant_speech.html')

def wordblocks(request):
    return render(request,'word_blocks.html')

def codebuster(request):
    return render(request,'codebuster.html')

def mathbuzz(request):
    return render(request,'math_buzz.html')
def jam(request):
    return render(request,'JAM.html')

def sodoku(request):
    return render(request,'sudoku.html')

def primesuspect(request):
    return render(request,'prime_suspect.html')

def tug(request):
    return render(request,'pulling_an_arrow.html')

def smashkarts(request):
    return render(request,'smash_karts.html')

def passthebomb(request):
    return render(request,'pass_the_bomb.html')
