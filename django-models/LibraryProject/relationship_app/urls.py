from django.urls import path
from .views import list_books, LibraryDetailView


app_name = 'relationship_app'
urlpatterns = [
    # path('', views.BookList.as_view(), name='list-books'),
    # path('librarydetail/<int:pk>/',
    #      views.LibraryDetail.as_view(), name='library-detail'),
    path('', list_books, name='list-books'),
    path('librarydetail/<int:pk>/',
         LibraryDetailView, name='library-detail'),

]
