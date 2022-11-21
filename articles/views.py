from django.shortcuts import render, redirect
from .models import Article, Search
from .forms import ArticleForm
from django.core.paginator import Paginator
from django.db.models import Q, Count  

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


def category(request, category):
    category_table = {
        "APPAREL": "APPAREL",
        "GAMES": "GAMES",
        "COLLECTIBLES": "COLLECTIBLES",
        "HOME & OFFICE": "HOME & OFFICE",
        "BOOKS": "BOOKS",
        "MUSIC & VIDEO": "MUSIC & VIDEO",
        "ARTS & POSTERS": "ARTS & POSTERS",
        "ACCESSORIES": "ACCESSORIES",
    }
    g_category = category_table.get(category)
    articles = Article.objects.filter(category=g_category)
    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(articles, 8)
    page_obj = paginator.get_page(page)
    print(articles)
    context = {
        "g_category": g_category,
        "articles": articles,
        "articles": page_obj,
    }
    return render(request, "articles/category.html", context)

def studio(request, studio):
    studio_table = {
        "STARDEW VALLEY": "STARDEW VALLEY",
        "X BOX": "X BOX",
        "PLAY STATION": "PLAY STATION",
        "ATLUS": "ATLUS",
        "HADES": "HADES",
        "RARE": "RARE",
    }
    
    g_studio = studio_table.get(studio)
    articles = Article.objects.filter(address__contains=g_studio)
    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(articles, 8)
    page_obj = paginator.get_page(page)
    context = {
        "g_studio": g_studio,
        "articles": articles,
        "articles": page_obj,
    }
    return render(request, 'articles/studio.html', context)




def search(request):
    searched = request.GET.get('searched')
    if not searched=="":
        if Search.objects.filter(keyword=searched).exists():
            search = Search.objects.get(keyword=searched)
            search.count += 1
            search.save()
        else:
            Search.objects.create(keyword=searched, count=1)
    articles = Article.objects.filter(
        Q(name__contains=searched)|
        Q(category__contains=searched)|
        Q(address__contains=searched)
        ).distinct().order_by('-name')
    articles_count = articles.count()
    # 입력 파라미터
    page = request.GET.get("page", "1")
    # 페이징
    paginator = Paginator(articles, 16)
    page_obj = paginator.get_page(page)
    context = {
        "searched": searched,
        "articles_count": articles_count,
        "articles": page_obj,
    }
    return render(request, 'articles/search.html', context)