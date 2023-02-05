from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse
from django.shortcuts import render, redirect


def user_list(request):
    return render(request, 'liveuser/user_list.html')


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user_list'))
        else:
            print(form.errors)
    return render(request, 'liveuser/sign_up.html', {'form': form})


def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect(reverse('user_list'))
        else:
            print(form.errors)
    return render(request, 'liveuser/log_in.html', {'form': form})


def log_out(request):
    logout(request)
    return redirect(reverse('liveuser:log_in'))