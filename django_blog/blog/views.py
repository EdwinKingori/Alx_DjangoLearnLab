from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post, Profile
from .forms import CustomUserCreationForm, ProfileForm, UserEmailForm
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
