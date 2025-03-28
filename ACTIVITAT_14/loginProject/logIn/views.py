from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PersonForm

def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def login(request):
    return HttpResponse("login page")
def user_form(request):
    form = PersonForm()
    context = {'form':form}
    return render(request, 'form.html', context)