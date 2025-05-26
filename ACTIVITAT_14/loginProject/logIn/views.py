from tabnanny import check

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from .forms import EmailAuth
from .models import Profile

def index(request):
    if not request.user.is_authenticated:
        return redirect('user_form')

    username = request.user.username
    return render(request, 'index.html', {'username': username})
def home(request):
    if not request.user.is_authenticated:
        return redirect('user_form')

    username = request.user.username
    context = {'username': username}
    return render(request, 'home.html', context)

def user_form(request):
    if request.method == "POST":
        form = EmailAuth(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return render(request, 'form.html', {'form': form, 'error': 'Email no registrado.'})

            user_auth = authenticate(username=user.username, password=password)
            if user_auth:
                login(request, user_auth)
                return redirect('index')
            else:
                return render(request, 'form.html', {'form': form, 'error': 'Contraseña incorrecta.'})
    else:
        form = EmailAuth()
    return render(request, 'form.html', {'form': form})

@require_POST
def logout(request):
    auth_logout(request)
    request.session.flush()
    return redirect('user_form')