from django.shortcuts import render, redirect, get_object_or_404
from .models import Review, Comment
from .forms import ReviewForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.

@login_required
def create(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
            return redirect('reviews:index')
    else:
        form = ReviewForm()
    context = {
        'form' : form,
    }
    return render(request, 'reviews/create.html' ,context)

def detail(request, pk):
    review = Review.objects.get(pk=pk)
    form = CommentForm()
    temp = review.comment_set.all()
    context = {
        'review' : review,
        'form' : form,
        'temp' : temp,
    }
    return render(request, 'reviews/detail.html', context)

@login_required
def update(request, pk):
    temp = get_object_or_404(Review, pk=pk)
    if request.user == temp.user:
        if request.method == "POST":
            form = ReviewForm(request.POST, request.FILES, instance=temp)
            if form.is_valid():
                form.save()
                return redirect('reviews:index')
        else:
            form = ReviewForm(instance=temp)
        context = {
            'form': form,
        }
    return render(request, 'reviews/update.html', context)

@login_required
def delete(request, pk):
    review = Review.objects.get(pk=pk)
    review.delete()
    return redirect('reviews:index')

@login_required
def like(request, pk):
    article = get_object_or_404(Review, pk=pk)
    if request.user in article.like_users.all():
        article.like_user.remove(request.user)
        is_liked = False
    else:
        article.like_user.add(request.user)
        is_liked = True
    context = {
        'is_liked' : is_liked,
        'like_count' : article.like_users.count()
    }
    return JsonResponse

@login_required
def comment_create(request, pk):
    article = get_object_or_404(Review, pk=pk)
    commentform = CommentForm(request.POST)
    if commentform.is_valid():
        comment = commentform.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
        context = {
            'content': comment.content,
            'username': comment.user.username
        }
        return JsonResponse(context)
    
@login_required
def comment_delete(request, pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.user == comment.user:
        comment.delete()
        return redirect('reviews:detail', pk)
    else:
        messages.warning(request, '본인의 댓글만 삭제할 수 있습니다.')
        return redirect('reviews:detail', pk)

def index(request):
    return render(request, 'reviews/index.html')