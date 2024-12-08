from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

urlpatterns = [
    # login and logout views
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),

    # registration
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    path('', views.index, name='home'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>/', views.PostUpdateview.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/comments/create/<int:pk>/',
         CommentCreateView.as_view(), name='add-comment'),
    path('comment/update/<int:pk>/',
         CommentUpdateView.as_view(), name='comment-edit'),
    path('comment/delete/<int:pk>/',
         CommentDeleteView.as_view(), name='comment-delete'),
    path('search/', search_posts, name='search'),
    path('tags/<slug:tag_slug>/',
         views.PostByTagListView.as_view(), name='posts-by-tag'),


]
