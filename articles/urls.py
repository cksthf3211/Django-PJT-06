from django.urls import path
from . import views


app_name = "articles"

urlpatterns = [
    path("", views.index, name="index"),
    path("shop/", views.shop, name="shop"),
    # path('', views.AllListView.as_view(), name='all_list'),
]
