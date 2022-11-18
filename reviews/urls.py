from django.urls import path
from . import views

app_name = "reviews"

urlpatterns = [
    path('create/', views.create, name='create'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('<int:pk>/like/', views.like, name='like'),
    path('<int:pk>/comments/create/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:comment_pk>/delete/', views.comment_delete, name='comment_delete'),
    path('', views.index, name='index'),
]
