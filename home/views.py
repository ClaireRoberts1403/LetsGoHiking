from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def index(request):

    return render(request, 'home/index.html')


def about(request):

    return render(request, 'home/about.html')


def contact(request):

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Message sent to the Lets Go Hiking team!')
            return redirect(reverse('home'))
    else:
        form = ContactForm()
        messages.error(request, f'Failed to send message')

    form = ContactForm()
    template = 'home/contact.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
