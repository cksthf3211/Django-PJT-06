from django.shortcuts import render, redirect
from .models import *

# Create your views here.


def index(request):
    return render(request, "articles/index.html")

def shop(request):
    return render(request, "articles/shop.html")

def main(request):
    return render(request, "articles/main.html")

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products':products})