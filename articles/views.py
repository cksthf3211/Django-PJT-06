from django.shortcuts import render, redirect

# Create your views here.


def index(request):
    return render(request, "articles/index.html")

def shop(request):
    return render(request, "articles/shop.html")

def main(request):
    return render(request, "articles/main.html")
