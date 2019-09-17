from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from clubbing.register import SignUpForm

def index(request):
    return render(request, 'index.html')

def logout_page(request):
    logout(request)
    return render(request, 'logout.html')

def login_page(request):
    # user = authenticate(request)
    # login(request, user)
    return render(request, 'login.html')

def login_page(request):
    # user = authenticate(request)
    # login(request, user)
    if request.method == 'GET':
        return render(request, 'login.html')
    elif request.method == 'POST':
        login_str = request.POST["login"]
        password_str = request.POST["password"]
        user = authenticate(username=login_str, password=password_str)
        if user is not None:
            login(request, user)
        return redirect('index')

def register_page(request):
    if request.method == 'GET':
        return render(request, 'register.html', context={'form': SignUpForm()})
    elif request.method == 'POST':
        return redirect('index')
