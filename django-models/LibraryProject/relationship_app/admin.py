from django.contrib import admin
from .models import Author, Librarian, Library, Book
# Register your models here.

admin.site.register(Author)
admin.site.register(Librarian)
admin.site.register(Library)
admin.site.register(Book)
