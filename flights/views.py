from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "flights/index.html")

def login(request):
    return render(request, "flights/login.html")

def signup(request):
    return render(request, "flights/signup.html")