from tabnanny import check

from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import login
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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            try:
                profile = Profile.objects.get(email=email)

                if profile.password == password:
                    request.session['profile_id'] = profile.id
                    request.session['authenticated'] = True
                    return redirect('index')
                else:
                    return render(request, 'form.html', {'form': form, 'error': 'Email o contraseña incorrectas.'})
            except Profile.DoesNotExist:
                print(f"No existe perfil para este email: {email}")
                return render(request, 'form.html', {'form': form, 'error': 'Email o contraseña incorrectas.'})
    else:
        form = EmailAuth()
    context = {'form': form}
    return render(request, 'form.html', context)