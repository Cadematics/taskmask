from django.shortcuts import render, redirect
from django.http import HttpResponse
# from django.contrib.auth.forms import UserCreationForm
from users_app.form import CustomRegisterForm
from django.contrib import messages
# Create your views here.

def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST)
        if register_form.is_valid():
            register_form.save()
        messages.success(request, ('New User Added!, Login to get started'))
        return redirect ('register_page')
    else:
        register_form = CustomRegisterForm()
        context = {
            'register_form': register_form
        }
    return render(request, 'register.html', context)
    