from django.conf import settings

class Cart():
    """
    """
    def __init__(self, request):
        """
        Initialize the Cart
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart: # if user has no session
            # save an empty cart in the session
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    
    def add(self, product, quantity=1):
        """
        Add and updateing the users basket session data
        """
        product_id = product.id

        if product_id not in self.cart:
            self.cart[product_id] = {"price":str(product.price), 'quantity': quantity}
        print("self.add")
        self.session.modified = True

    def __len__(self):
        """
        Count all items in the cart.
        """
        return sum(item['quantity'] for item in self.cart.values())