from django.contrib import admin
from django.urls import path,include
from . import views
from .views import PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [
    path('', views.home,name="post-home"),
    path('explore/',views.explore,name="post-explore"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('share/',views.share,name="post-share"),
    path('payment/',views.explorepay,name="post-pay"),
    path('charge/', views.charge, name="charge"),
    path('success/<str:args>/', views.successMsg, name="success"),
]