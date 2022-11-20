from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("articles/", views.index, name="index"),
    path("articles/shop/", views.shop, name="shop"),
    path("", views.main, name="main"),
    path('articles/create/', views.create, name='create'),
   	path("articles/<int:pk>/", views.detail, name="detail"),
    path("articles/<int:pk>/update/", views.update, name="update"),
    path("articles/<int:pk>/delete/", views.delete, name="delete"),
    # path('', views.AllListView.as_view(), name='all_list'),
]
