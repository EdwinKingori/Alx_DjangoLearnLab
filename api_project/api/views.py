from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import viewsets
from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  # use bookserializer for serializatin
    authentication_classes = [TokenAuthentication]
    # Only authenticated users can access
    permission_classes = [IsAuthenticated]


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  # use bookserializer for serializatin
    authentication_classes = [TokenAuthentication]
    # Only authenticated users can access
    permission_classes = [IsAuthenticated]
