from django.urls import path
from .views import list_books, LibraryDetailView, register, login, logout, LoginView, LogoutView


app_name = 'relationship_app'
urlpatterns = [
    # path('', views.BookList.as_view(), name='list-books'),
    # path('librarydetail/<int:pk>/',
    #      views.LibraryDetail.as_view(), name='library-detail'),

    # Login view with custom template
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),

    # Logout view with custom template
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),


    path('', list_books, name='list-books'),
    path('librarydetail/<int:pk>/',
         LibraryDetailView, name='library-detail'),
    path('register', register, name='register'),
    path('login', login, name='login'),
    path('logout', logout, name='logout'),


]
