from django.urls import path
from . import views


app_name = 'relationship_app'
urlpatterns = [
    # path('', views.BookList.as_view(), name='list-books'),
    # path('librarydetail/<int:pk>/',
    #      views.LibraryDetail.as_view(), name='library-detail'),
    path('', views.bookList, name='list-books'),
    path('librarydetail/<int:pk>/',
         views.libraryDetail, name='library-detail'),

]
