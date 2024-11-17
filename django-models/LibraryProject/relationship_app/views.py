from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Library, Book
# Create your views here.


class LibraryDetail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'


class BookList(ListView):
    model = Book
    template_name = 'relationship_app/list_books.html'
