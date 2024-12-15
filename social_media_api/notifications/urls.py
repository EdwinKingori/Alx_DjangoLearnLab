from django.urls import path
from .views import LikePostView, UnlikePostView, NotificationListView
urlpatterns = [
    path('posts/<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('posts/<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    path('notifications/', NotificationListView.as_view(),
         name='notifications-list'),
]
