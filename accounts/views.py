from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from store.models import Customer
from django.contrib import messages
# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'store/login.html')

def register_view(request):
    if request.method == 'POST':
        
        first_name = request.POST['first_name']
        last_name = request.POST.get('last_name', False)
       
                
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        
        if password1 == password2 :
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = password1, email = email, 
                        first_name = first_name, last_name = last_name)
                user.save()
                customer = Customer()
                customer.user = user
                customer.name = username
                customer.email = email
                customer.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'Passwords not matched')
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'store/register.html')

def logout_view(request):
    logout(request)
    return redirect('/')