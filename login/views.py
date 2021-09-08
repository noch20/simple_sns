from django.contrib import auth
from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        username = request.user.username
    else:
        username = ""
    return render(request, "login/home.html", {'is_authenticated': request.user.is_authenticated, 'username': username})

def logon(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('login:home')

    form = UserCreationForm()
    return render(request, 'login/logon.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('login:home')
        
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('login:home')