from django.contrib import admin
from .models import Author, Book
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year',)
    search_fields = ('title', 'author',)
    list_filter = ('publication_year',)


admin.site.register(Author)
admin.site.register(Book, BookAdmin)
