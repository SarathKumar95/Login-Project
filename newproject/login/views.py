from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
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

        

        if pass1 == pass2:

            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Taken. Please try some other username')
                return redirect('signup')
            
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'A user already exists on that email address.')
                return redirect('signup')

            else:
                
                my_user = User.objects.create_user(username, email, pass1)
                
                my_user.save()
                
                messages.success(request, 'Your account has been created!.You can log in now.')

                return redirect('index')
        
        else:
            messages.info(request,"Passwords don't match.Try again.")
            return redirect('signup')


def signin(request):

    if request.method == 'GET':
        return render(request,'index.html')

    if request.method == 'POST':

        username = request.POST['uname']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        context = {"username":username}

        if user is not None:
                return render(request,'home.html',context)
            
        else:
            messages.info(request,'Check username or password.')
            print('User does not exist')
            return render(request,'index.html')


def home(request):
    return render(request,'home.html')



def signout(request):
        logout(request)
        return render(request, 'index.html')
    
