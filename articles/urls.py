from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("articles/", views.index, name="index"),
    path("articles/shop/", views.shop, name="shop"),
    path("", views.main, name="main"),
    path('articles/create/', views.create, name='create'),
    # path('', views.AllListView.as_view(), name='all_list'),
]
