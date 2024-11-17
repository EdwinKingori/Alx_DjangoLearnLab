from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Library, Book
# Create your views here.


# class LibraryDetail(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'


# class BookList(ListView):
#     model = Book
#     template_name = 'relationship_app/list_books.html'


def bookList(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


def libraryDetail(request, pk):
    library = Library.objects.get(id=pk)
    context = {
        'library': library
    }
    return render(request, 'relationship_app/library_detail.html', context)
