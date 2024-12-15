from .models import Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    class meta:
        model = Post
        fields = ['id', 'author', 'title',
                  'content', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    class meta:
        model = Comment
        fields = ['id', 'post', 'author',
                  'content', 'created_at', 'updated_at']
