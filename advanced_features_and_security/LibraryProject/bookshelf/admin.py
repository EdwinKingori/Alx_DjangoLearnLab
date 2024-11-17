from .models import CustomUser
from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Book, customuser
from django.contrib.auth.admin import UserAdmin
# Register your models here.


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    search_fields = ('title' 'author')
    list_filter = ()


admin.site.register(Book, BookAdmin)


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
