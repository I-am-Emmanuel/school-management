from django.shortcuts import render
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()}

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    

