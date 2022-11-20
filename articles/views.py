from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.


def index(request):
    articles = Article.objects.all()[:8]

    return render(
        request,
        "articles/index.html",
        {
            "articles": articles,
        },
    )
    
def shop(request):
    return render(request, "articles/shop.html")

def main(request):
    return render(request, "articles/main.html")

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user=request.user
            article.save()
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


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    return render(
        request,
        "articles/detail.html",
        {
            "article": article,
        },
    )


def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        if request.method == "POST":
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                form.save()
                return redirect("articles:detail", article.pk)
        else:
            form = ArticleForm(instance=article)
        return render(
            request,
            "articles/update.html",
            {
                "form": form,
            },
        )
    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden()


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.user == article.user:
        article.delete()
    else:
        from django.http import HttpResponseForbidden

        return HttpResponseForbidden()
    return redirect("articles:index")