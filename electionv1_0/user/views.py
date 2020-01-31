from django.contrib import admin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import UserForm

def index(request):
    return render(request, 'user/index.html')

@login_required
def special(request):
    return HttpResponse("You are logged in!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
            return render(request, 'user/login.html', {})
    else:
        user_form = UserForm()
        context={'user_form': user_form, 
                'registered': registered
                }
        return render(request, 'user/registration.html', context)

def user_login(request):
    if request.method == 'POST':
        citizenship_number = request.POST.get('citizenship_number')
        password = request.POST.get('password')
        user = authenticate(citizenship_number=citizenship_number, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Your account was inactive")
        else:
            print('Someone tried to login and failed.')
            print("They used email: {} and password: {}".format(email, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'user/login.html', {})