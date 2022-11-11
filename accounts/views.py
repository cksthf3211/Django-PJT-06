from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, authenticate
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("articles:index")
        else:
            print("error")
            print(form.error_messages)
    else:
        form = CustomUserCreationForm
    context = {
        "form": form,
    }
    return render(request, "accounts/signup.html", context)


def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
        else:
            messages.warning(request, "아이디 또는 비밀번호가 틀렸습니다.")
        return redirect(request.GET.get("next") or "articles:index")
    else:
        form = AuthenticationForm()
        context = {
            "form": form,
        }
        return render(request, "accounts/login.html", context)


def logout(request):
    auth_logout(request)
    return redirect("articles:index")


@login_required
def detail(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    context = {
        "user": user,
    }
    return render(request, "accounts/detail.html", context)


@login_required
def profile_update(request):
    if request.method == "POST":
        form = CustomUserChangeForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect("accounts:detail", request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
def password_update(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  ## 비밀번호 변경 후 로그아웃 방지
            return redirect("accounts:detail", request.user.pk)
    else:
        form = PasswordChangeForm(request.user)
    context = {
        "form": form,
    }
    return render(request, "accounts/update.html", context)


@login_required
@require_POST
def delete(request):
    try:
        request.user.delete()
        auth_logout(request)
        messages.success(request, "탈퇴하셨습니다.")
    except:
        messages.error(request, "error")
        return render(request, "articles:index")
    return redirect("articles:index")
