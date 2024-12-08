from django.contrib import admin
from .models import Post, Profile
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'published_date']


class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user']


admin.site.register(Post, PostAdmin)
admin.site.register(Profile, ProfileAdmin)
