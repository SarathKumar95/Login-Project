from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import  messages


# Create your views here.

def home(request):
    return render(request, 'index.html')


def signup(request):
    if request.method == "GET":
        return render(request, 'signup.html')

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        my_user = User.objects.create_user(username, email, pass1)

        my_user.save()

        messages.success(request, 'Your account has been created!')

        return redirect('index.html')


