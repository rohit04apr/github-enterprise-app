from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import subprocess as sub
import os
import time

# Create your views here.
def home(request):
    return render(request, 'authenticate/home.html', {})


#def login_user(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#                login(request, user)
#                messages.success(request, ('You Have Been Logged In!'))
#                return redirect('home')
#
#        else:
#                messages.success(request, ('Error loggin. Please try again!'))
#                return redirect('login')
#
#    else:
#        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ('You Have Been Logged Out!'))
    return redirect('home')

def unlock(request):
    username = request.POST['username']
    command = "ssh -oStrictHostKeyChecking=no admin@<dns> -p 122 'ghe-user-unsuspend %s'" % (username)
    #command = "date; sleep 10;"
    p = sub.Popen(command, stdout = sub.PIPE, stderr = sub.PIPE, shell=True, universal_newlines=True)
    output, errors = p.communicate()
    print(command)
    print(output)
    print(errors)


    return render(request, 'authenticate/home.html', {'output': output, 'errors': errors})
