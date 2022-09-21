from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse

from store.models import Product
from .cart import Cart

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'cart/summary.html', {'cart': cart})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        # Get product ID
        product_id = int(request.POST.get("product_id"))
        product_qty = int(request.POST.get("product_qty"))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity = cart.__len__()
        response = JsonResponse({'product_quantity': cart_quantity})
        return response
    

def cart_delete(request):
    cart = Cart(request)
    print(request.POST)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get("product_id"))
        cart.remove(product_id=product_id)
        
        cart_quantity = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'quantity': cart_quantity, 'subtotal': carttotal})
        return response


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'POST':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        cart.update(product_id=product_id, quantity=product_qty)

        cart_quantity = cart.__len__()
        carttotal = cart.get_total_price()
        response = JsonResponse({'quantity': cart_quantity, 'subtotal': carttotal})
        return response