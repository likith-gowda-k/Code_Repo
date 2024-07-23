from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import WatchesUploads,Wishlist, Cart
from .forms import UploadForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def Home(request):
    watches = WatchesUploads.objects.all()
    context = {'watches_t' : watches}
    return render(request, "home.html", context)

def About(request):
    return render(request, "about.html")

@login_required(login_url="/login")
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

from django.shortcuts import get_object_or_404
def show_product(request,id):
    product = get_object_or_404(WatchesUploads, id=id)
    return render(request, 'product.html', {'product': product})

def addtowish(request,id):
    user= request.user
    product= WatchesUploads.objects.get(id=id)
    obj1,created = Wishlist.objects.get_or_create(user=user)
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

def addtocart(request,id):
    user=request.user
    product= WatchesUploads.objects.get(id=id)
    obj1,created = Cart.objects.get_or_create(user=user)
    obj1.save()
    obj1.products.add(product)
    obj1.save()
    return redirect('home')

@login_required(login_url="/login")
def show_wishlist(request):
    user = request.user
    wish_object = Wishlist.objects.get(user=user)
    return render(request, 'wishlist.html', {'user_products': wish_object.products.all()})

@login_required(login_url="/login")
def show_cart(request):
    user = request.user
    cart_object = Cart.objects.get(user=user)
    return render(request, 'cart.html', {'cart_products': cart_object.products.all()})


    


