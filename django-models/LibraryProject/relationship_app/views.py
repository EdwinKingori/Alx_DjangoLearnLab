from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views import View
from .models import Library, Book


from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


# class LibraryDetail(DetailView):
#     model = Library
#     template_name = 'relationship_app/library_detail.html'


# class BookList(ListView):
#     model = Book
#     template_name = 'relationship_app/list_books.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def user_logout(request):
    logout(request)
    return render(request, 'logout.html')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Account created successfully! You can now log in.')
            return redirect('login')
        else:
            messages.error(
                request, 'Error creating account. Please check the details and try again.')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})


def list_books(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


class LoginView():
    pass


class LogoutView():
    pass


def LibraryDetailView(request, pk):
    library = Library.objects.get(id=pk)
    context = {
        'library': library
    }
    return render(request, 'relationship_app/library_detail.html', context)
