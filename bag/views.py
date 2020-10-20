from django.shortcuts import render


def bag(request):

    return render(request, 'bag/bag.html')
