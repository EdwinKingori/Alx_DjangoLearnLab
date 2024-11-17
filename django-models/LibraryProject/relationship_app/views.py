from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from .models import Library, Book
# Create your views here.


# class LibraryDetail(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'


# class BookList(ListView):
#     model = Book
#     template_name = 'relationship_app/list_books.html'


def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


def LibraryDetailView(request, pk):
    library = Library.objects.get(id=pk)
    context = {
        'library': library
    }
    return render(request, 'relationship_app/library_detail.html', context)
