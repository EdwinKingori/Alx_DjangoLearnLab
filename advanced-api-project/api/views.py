from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import BookSerializer
from .models import Book
from django.shortcuts import render
from rest_framework import generics, mixins
from rest_framework import viewsets
from django_filters import rest_frameworks
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny
from rest_framework.response import Response
# Create your views here.


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow unauthenticated users to view the list
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'author__name', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    def get(self, request):
        return Response({"message": "This endpoint is accessible by anyone."})

# DetailView to retrieve a single book by ID


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow unauthenticated users to view book details
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "This endpoint is accessible by anyone."})

# CreateView to add a new book


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can create books
    permission_classes = [IsAuthenticated]


# UpdateView to modify an existing book
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can update books
    permission_classes = [IsAuthenticated]


# DeleteView to remove a book
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Only authenticated users can delete books
    permission_classes = [IsAuthenticated]
