from django.urls import path
from django.contrib.auth import views as auth_views
from .import views
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    CommentCreateView,
    CommentUpdateView,
    CommentDeleteView
)

urlpatterns = [
    # login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # registration
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('', views.index, name='home'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:pk>/comments/new/',
         CommentCreateView.as_view(), name='add-comment'),
    path('comment/<int:pk>/update/',
         CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/<int:pk>/delete/',
         CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', views.search_posts, name='search'),
    path('tags/<slug:tag_slug>/',
         views.PostByTagListView.as_view(), name='posts-by-tag'),


]
