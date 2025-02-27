from django.shortcuts import render
from django.http import HttpResponseServerError

# Create your views here.
from urllib import request
from django.shortcuts import redirect, render
# from signup.models import *
from django.contrib.auth.models import User,Group
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
import socket


def signinUser(request):
    user = request.user
    # if request.user.is_authenticated:
    #     return redirect("signin")
    context = {}
    try:
        if request.method == 'POST':
            fname=request.POST.get("first_name")
            lname=request.POST.get("last_name")
            email=request.POST.get("email")
            username=request.POST.get("username")
            password1=request.POST.get("password1")
            password2=request.POST.get("password2")

            # print("Than correct!")
            if User.objects.filter(username=username).first():
                messages.error(
                    request, "This username is already taken! Please login with user id!")
                return redirect('signup')
            if User.objects.filter(email=email).first():
                messages.error(
                    request, "This email is already taken! Please login with user id")
                return redirect('signup')
            if password1 == password2:
                fname=request.POST.get("first_name")
                lname=request.POST.get("last_name")
                email=request.POST.get("email")
                username=request.POST.get("username")
                password1=request.POST.get("password1")
                password2=request.POST.get("password2")

                user = User.objects.create_user(
                    username=username, email=email, password=password1, first_name=fname, last_name=lname)
                user.save()
                return redirect("login")
            else:
                messages.warning(request, 'Password must be same!')
                return render(request, "authent/submit.html", context)
        else:
            return render(request, "authent/submit.html", context)
    except socket.gaierror:
        return HttpResponseServerError("Internet connection error")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"Login Successfully!!")
            return redirect("home")
        else:
            messages.warning(request,"User or password is not correct!")

    return render(request, "authent/login.html")


def logOutUser(request):
    logout(request)
    return redirect("home")
