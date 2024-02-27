from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('', lambda request: redirect('article/1', permanent=True), name = 'home'),
    path('article/<int:pk>', views.ArticleView.as_view(), name='article-detail'),
]