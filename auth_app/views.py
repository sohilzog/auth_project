from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib import auth
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request,'home.html')
def adminpage(request):
    return render(request,'admin.html')


@login_required(login_url='login1')
def cart(request):
    # if 'uid' in request.session:        session
    # if request.user.is_authenticated:      is_authenticated
        return render(request,'cart.html')
    # else:
        return redirect('loginpage')  # ← Now this works!




def reg(request):
    if request.method=='POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        cpassword = request.POST.get('confirm_password')
        email = request.POST.get('email')

        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
                return render(request, 'register.html')  # Stay on form
            else:
                user = User.objects.create_user(
                    username=username,  # username/password FIRST
                    password=password,
                    first_name=first_name,
                    last_name=last_name,
                    email=email
                )
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('loginpage')  # ← Now this works!
        else:
            messages.error(request, 'Passwords do not match!')
            return render(request, 'register.html')  # Stay on form
    
    return render(request, 'register.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_staff==1:
                 login(request,user)
                 return redirect('adminpage')
            else:

                auth.login(request, user)
                messages.info(request, f'welcome {username}')
                return redirect('about')
        else:
            messages.info(request, "Invalid username or password")
            return redirect('loginpage')

    return render(request, 'login.html')


@login_required(login_url='login1')
def logout(request):
    if request.user.is_staff:
        auth.logout(request)
        messages.success(request, 'Admin logout successful')
        return redirect('login1') 
    else:
    # if request.user.is_authenticated:     is authenticated

    # request.session['uid']=" "     session
    
        auth.logout(request)
        messages.info(request,'logout success')
        return redirect('home')
    
    # else:
            # return redirect('loginpage')
          


def about(request):
    return render(request, 'about.html')
        
        






