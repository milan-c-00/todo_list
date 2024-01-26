from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'accounts/home.html')


def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password_confirmation']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password'])
                auth.login(request, user)
                return redirect('all_tasks')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match!'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('all_tasks')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials!'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')


