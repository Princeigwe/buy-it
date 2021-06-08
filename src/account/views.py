from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm
## importing django's default UUser Registration form
## from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):
    if request.method == "POST":
        register_form = UserRegistrationForm(request.POST)
        if register_form.is_valid():
            new_user = register_form.save(commit=False)
            new_user.set_password( register_form.cleaned_data['password2'] )
            new_user.save()
            # redirecting to the same page for the login
            return render(request, 'registration/login.html', {'new_user': new_user})
    else:
        register_form = UserRegistrationForm()
    return render(request, 'registration/login.html', {'register_form': register_form})
    