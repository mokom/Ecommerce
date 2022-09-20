from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from store.models import Product
from .cart import Cart

def cart_summary(request):
    return render(request, 'cart/summary.html')

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
    