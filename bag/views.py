from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from shop.models import product


def bag(request):

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):

    Product = get_object_or_404(product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


# def adjust_bag(request, item_id):
#
#    Product = get_object_or_404(product, pk=item_id)
#    quantity = int(request.POST.get('quantity'))
#
#    if quantity > 0:
#        bag[item_id] = quantity
#        messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
#    else:
#        bag.pop(item_id)
#        messages.success(request, f'Removed {product.name} from your cart')
#
#    request.session['bag'] = bag
#    return redirect(reverse('view_bag'))


# def remove_from_bag(request, item_id):
#
#    try:
#        Product = get_object_or_404(product, pk=item_id)
#        bag.pop(item_id)
#        messages.success(request, f'Removed {product.name} from your cart')
#        request.session['bag'] = bag
#        return HttpResponse(status=200)
#
#    except Exception as e:
#        messages.error(request, f'Error removing item: {e}')
#        return HttpResponse(status=500)
