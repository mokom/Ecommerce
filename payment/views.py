import json

import stripe
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView

from cart.cart import Cart
from orders.views import payment_confirmation


def order_placed(request):
    cart = Cart(request)
    cart.clear()
    return render(request, 'payment/orderplaced.html')


class Error(TemplateView):
    template_name = 'payment/error.html'


@login_required
def CartView(request):

    cart = Cart(request)
    total = str(cart.get_total_price())
    total = total.replace('.', '')
    total = int(total)

    print(total)

    stripe.api_key = 'sk_test_51JCUg3KvELx4Sm5hfSomtogvUhgSZTH0bTL8AIO3tA3os8jQYXVxiDlJSD7ao07xiuwCLcZI2rIb4oCxaDTLI2DZ00KEgxP5bQ'
    intent = stripe.PaymentIntent.create(
        amount=total, #amt to send
        currency='gbp',
        metadata={'userid': request.user.id} # Used to match up order with user
    ) # intent returns a client key from stripe each time a payment is made 

    return render(request, 'payment/payment.html', {'client_secret': intent.client_secret})


@csrf_exempt
def stripe_webhook(request):
    payload = request.body
    event = None

    try:
        event = stripe.Event.construct_from(
            json.loads(payload), stripe.api_key
        )
    except ValueError as e:
        return HttpResponse(status=400)

    # Handle the event
    if event.type == 'payment_intent.succeeded':
        print("payment was successful")
        payment_confirmation(event.data.object.client_secret)

    else:
        print('Unhandled event type {}'.format(event.type))

    return HttpResponse(status=200)