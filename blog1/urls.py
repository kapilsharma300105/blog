from django.urls import path,include
from . import views

from .views import PostCreateView, PostUpdateView, PostDeleteView
from .views import (
    PostListView,
    UserPostListView,
    postDetailView,
)
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('user/<str:username>/', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', postDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),

]