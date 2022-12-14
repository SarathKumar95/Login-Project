from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import  messages
from django.contrib.auth import authenticate
from django.views.decorators.cache import cache_control


# Create your views here.

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

                return redirect('signin')
        
        else:
            messages.info(request,"Passwords don't match.Try again.")
            return redirect('signup')

@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def signin(request):

    if 'username' in request.session:
        return redirect(home)

    if request.method == 'POST':

        username = request.POST['uname']
        password = request.POST['password']

        print("Username is",username)

        user = authenticate(username = username, password = password)

        if user is not None:
                request.session['username'] = username
                return redirect(home)
            

            
        else:
            messages.info(request,'Check username or password.')
            print('User does not exist')
            return render(request,'index.html')
    
    return render(request,'index.html')


@cache_control(no_cache=True,must_revalidate=True,no_store=True)
def home(request):
    if 'username' in request.session:
        temp = {"username":request.session['username']}
        context = {'temp':temp}
        return render(request,'home.html',context)
    return redirect(signin)



def signout(request):
    if 'username' in request.session:
        request.session.flush()
    return redirect(signin)
