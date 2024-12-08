from .models import Comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def save(self, commit=True):
        # Calling the parent save method with commit=False.
        user = super().save(commit=False)
        # Assigning the email field from the cleaned data.
        user.email = self.cleaned_data['email']
        if commit:
            user.save()  # saving the user instance to the database
        return user  # returning the user instance


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']


class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']


class PostForm(forms.ModelForm):
    #tags = TagField(widgets=TagWidget())

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
