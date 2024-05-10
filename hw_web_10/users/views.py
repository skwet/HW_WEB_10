from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('quotes:quotes_list')  
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    return redirect('quotes:quotes_list')  
