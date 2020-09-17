
from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from . models import *
from django.contrib import messages
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from django.contrib.auth import logout, login
from django.core.files.storage import FileSystemStorage
from .forms import *

# Create your views here.


def index(request):
    if request.user.is_authenticated:
        # Do something for authenticated users.

        if request.method == 'POST':
            form = Profile_Form(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                new_form = Profile_Form()
                # Get the current instance object to display in the template

                return render(request, 'home.html', {'form': new_form})
        else:
            form = Profile_Form()
        return render(request, 'home.html', {'form': form})

    else:
        # Do something for anonymous users.

        return signin(request)


def picture_view(request):
    pic = Userupdate.objects.all()
    return render(request, "view.html", {'pic': pic})


def signin(request):

    if request.method == 'GET':
        print('in get method')
        if request.user.is_authenticated:
            return render(request, 'home.html')
        else:
            return render(request, 'signin.html')
    else:
        print('In post method')
        username = request.POST['username']
        password = request.POST['password']
        print(username, password)
        user = authenticate(username=username, password=password)
        if not user:
            messages.error(request, 'Please check your username and password')
            return render(request, 'signin.html')

        else:

            user.last_login = datetime.today()
            user.save()
            request.session['is_logged'] = True
            request.session['username'] = username
            login(request, user)

            return render(request, "home.html")


def signout(request):
    logout(request)
    return index(request)
