from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from .serializers import BookSerializer, AuthorSerializer
from .models import Author, Book
# Create your views here.
