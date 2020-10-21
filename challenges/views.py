from django.shortcuts import render, redirect, reverse
from .models import challenge
from .forms import challengeForm


def challenges(request):
    challenges = challenge.objects.all()

    return render(request, 'challenges/challenges.html', {'challenges': challenges})


# Login in required needs adding/confirmation of payment


def full_challenge(request):
    challenges = challenge.objects.all()

    return render(request, 'challenges/full_challenge.html', {'challenges': challenges})


def add_challenge(request):

    if request.method == 'POST':
        form = challengeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse('add_challenge'))
    else:
        form = challengeForm()

    form = challengeForm()
    template = 'challenges/add_challenge.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
