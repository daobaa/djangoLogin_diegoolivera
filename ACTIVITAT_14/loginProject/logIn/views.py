from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate
from django.http import HttpResponse
from django.template import loader
from .forms import EmailAuth

User = get_user_model()

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def user_form(request):
    if request.method == "POST":
        form = EmailAuth(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                user = None
            if user is not None:
                user = authenticate(request, username=user.username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                return render(request, 'form.html', {'form': form, 'error': 'Email o contraseña incorrectos'})
    else:
        form = EmailAuth()
    context = {'form': form}
    return render(request, 'form.html', context)