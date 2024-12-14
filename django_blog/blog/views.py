from django.db.models import Q
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Post, Profile, Comment, Tag
from .forms import CustomUserCreationForm, ProfileForm, UserEmailForm, CommentForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Your account has been Created! You can now login.")
            return redirect("login")
        else:
            messages.error(
                request, 'There was an error with your registration. Please try again.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/registration.html')


@login_required(login_url='/login/')
def profile(request):
    user = request.user
    try:
        profile = user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=user)

    user_form = UserEmailForm(instance=user)
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        user_form = UserEmailForm(request.POST, instance=user)
        profile_form = ProfileForm(
            request.POST, request.FILES, instance=profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            user_form = UserEmailForm(instance=user)
            profile_form = profile_form(instance=profile)

    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }

    return render(request, 'registration/profile.html', context)


def index(request):
    return render(request, 'blog/home.html')


class PostListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'blog/post_create.html'

    def for_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateview(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = "blog/post_update.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('posts')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostByTagListView(ListView):
    model = Post
    template_name = 'blog/post_list_by_tag.html'  
    context_object_name = 'posts'

    def get_queryset(self):
        # Filter posts by the tag passed in the URL
        tag_slug = self.kwargs.get('tag_slug')
        tag = get_object_or_404(Tag, slug=tag_slug)
        return Post.objects.filter(tags__in=[tag])

    def get_context_data(self, **kwargs):
        # Add the tag to the context for template use
        context = super().get_context_data(**kwargs)
        context['tag'] = get_object_or_404(
            Tag, slug=self.kwargs.get('tag_slug'))
        return context


@login_required
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        # Automatically assign the current post and user to the comment
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail page after comment creation
        return self.object.post.get_absolute_url()

# configuring the search application


def search_posts(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query) | Q(
            tags__name__icontains=query)
    ).distinct()
    context = {
        {
        'query': query,
        'results': results
        }
    }
    return render(request, 'blog/search_results.html', context)


def posts_by_tag(request, tag):
    tag = get_object_or_404(Tag, slug=tag)
    posts = Post.objects.filter(tags__in=[tag])
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})


@login_required
class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        # Automatically assign the current post and user to the comment
        form.instance.post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        # Redirect to the post detail page after comment creation
        return self.object.post.get_absolute_url()


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def get_success_url(self):
        return self.object.post.get_absolute_url()

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
