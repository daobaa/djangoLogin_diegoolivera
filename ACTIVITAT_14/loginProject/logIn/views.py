from tabnanny import check

from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import check_password
from .forms import EmailAuth
from .models import Profile

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
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
