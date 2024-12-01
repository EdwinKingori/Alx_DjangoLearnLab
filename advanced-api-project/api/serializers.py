from rest_framework import serializers
from .models import Author, Book
from datetime import date


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']

    def validate_publication_year(self, value):

        if value > 2024:
            raise serializers.ValidationError(
                "Publication date cannot be in the future!")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)  # nested bookserializer

    class Meta:
        fields = ['name']
