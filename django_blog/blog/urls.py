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

]
