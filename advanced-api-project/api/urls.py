from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView

# router = DefaultRouter()
# router.register(r'books_create', BookCreateView, basename='book-create')


urlpatterns = [
    #     path('', include(router.urls)),
    #     path('api/token/', obtain_auth_token, name='api-token-auth'),

    path('books/', BookListView.as_view(), name='book-list'),  # GET all books
    path('books/<int:pk>/', BookDetailView.as_view(),
         name='book-detail'),  # GET book by ID
    path('books/create/', BookCreateView.as_view(),
         name='book-create'),  # POST to create a new book
    path('books/update/', BookUpdateView.as_view(),
         name='book-update'),  # PUT/PATCH to update a book
    path('books/delete/', BookDeleteView.as_view(),
         name='book-delete'),  # DELETE to remove a book
]
