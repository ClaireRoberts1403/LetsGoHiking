from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm


def profiles(request):

    return render(request, 'profiles/profiles.html')


def my_order_history(request):

    return render(request, 'profiles/my_order_history.html')


def my_challenges(request):

    return render(request, 'profiles/my_challenges.html')


@login_required
def userprofile(request):

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profiles)
    orders = profiles.orders.all()

    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, 'profiles/profiles.html', context)
