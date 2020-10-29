from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm
from challenges.models import challenge
from challenges.forms import ChallengeForm


@login_required
def profiles(request):

    profile = get_object_or_404(UserProfile, user=request.user)
    if request.method == 'GET':
        form = UserProfileForm(request.GET, request.FILES)
    else:
        form = UserProfileForm()

    return render(request, 'profiles/profiles.html')


@login_required
def my_order_history(request):

    return render(request, 'profiles/my_order_history.html')


@login_required
def my_challenges(request):

    return render(request, 'profiles/my_challenges.html')


@login_required
def edit_profile(request):

    is_superuser = request.user.is_superuser

    if not is_superuser:
            form.base_fields['user'].disabled = True

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('profiles'))
    else:
        form = UserProfileForm()

    form = UserProfileForm()
    template = 'profiles/edit_profile.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def submit_idea(request):
    if request.method == 'POST':
        form = ChallengeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('profiles'))
    else:
        form = ChallengeForm()

    form = ChallengeForm()
    template = 'profiles/submit_idea.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
