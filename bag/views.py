from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from django.contrib.sessions.models import Session
from products.models import Product

# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')

def add_to_bag(request,item_id):
    """ Add a quantity of the specified product to the shopping bag """
    product = Product.objects.get(pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    
    bag = request.session.get('bag', {})


    if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {product.name} quantity to {bag[item_id]}')
    else:
            bag[item_id] = quantity
            messages.success(request, f'Added{product.name} to your bag')
        
        
    request.session['bag'] = bag
    
    return redirect(redirect_url)