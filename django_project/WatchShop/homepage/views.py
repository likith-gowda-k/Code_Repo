from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Watches
from .forms import UploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    watches = Watches.objects.all()
    context = {'watches_t' : watches}
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")

@login_required
def Upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadForm()

    return render(request, "WatchUpload.html", {'form': form})


from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login, logout
def login_page(request):
    if request.method == "POST":
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user_name = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username= user_name, password = password)

            if user is not None: 
                login(request,user)
                return redirect('home')
            return  render(request, "login.html", {'form': form})


    else:
        form = AuthenticationForm()

    return render(request, "login.html", {'form': form})


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('home')