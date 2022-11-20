from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    return render(request, "articles/index.html")

def shop(request):
    return render(request, "articles/shop.html")

def main(request):
    return render(request, "articles/main.html")

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("articles:index")
    else:
        form = ArticleForm()
    return render(
        request,
        "articles/create.html",
        {
            "form": form,
        },
    )