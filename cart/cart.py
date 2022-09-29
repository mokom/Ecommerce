from decimal import Decimal

from django.conf import settings
from store.models import Product


class Cart:
    """ """

    def __init__(self, request):
        """
        Initialize the Cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:  # if user has no session
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1):
        """
        Add and updateing the users basket session data
        """
        product_id = str(product.id)

        if product_id in self.cart:  # should product be added from the single product page
            self.cart[product_id]["quantity"] = quantity
        else:
            self.cart[product_id] = {"price": str(product.price), "quantity": quantity}

        self.save()

    def __iter__(self):
        """
        Iterate over the items in the cart and get the products
        from the database.
        """
        product_ids = self.cart.keys()
        # get the product objects and add them to the cart
        products = Product.products.filter(id__in=product_ids)
        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product
        for item in cart.values():
            item["price"] = Decimal(item["price"])
            item["total_price"] = item["price"] * item["quantity"]
            yield item

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item["quantity"] for item in self.cart.values())

    def get_total_price(self):
        subtotal = sum(Decimal(item["price"]) * item["quantity"] for item in self.cart.values())

        if subtotal == 0:
            shipping = Decimal(0.00)
        else:
            shipping = Decimal(11.50)

        total = subtotal + Decimal(shipping)

        return total

    def remove(self, product_id):
        """
        Remove product from cart
        """
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def update(self, product_id, quantity):
        """
        Update values in session data
        """
        product_id = str(product_id)

        if product_id in self.cart:
            self.cart[product_id]["quantity"] = quantity

        self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.CART_SESSION_ID]
        self.save()

    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True
