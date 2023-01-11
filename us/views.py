from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth import login ,authenticate


def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = user.authenticate(username=username , password=password)
            login(request,user)
            return redirect('profile')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html', {'form':form})

def profile(request):
    pass