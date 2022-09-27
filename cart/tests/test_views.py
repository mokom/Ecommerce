from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestBasketView(TestCase):
    def setUp(self):
        User = get_user_model()
        User.objects.create(email='admin@admin.com')
        Category.objects.create(name='django', slug='django')
        Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django intermediate', created_by_id=1,
                               slug='django-intermediate', price='20.00', image='django')
        Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                               slug='django-advanced', price='20.00', image='django')
        self.client.post(
            reverse('cart:cart_add'), {"product_id": 1, "product_qty": 1, "action": "POST"}, xhr=True)
        self.client.post(
            reverse('cart:cart_add'), {"product_id": 2, "product_qty": 2, "action": "POST"}, xhr=True)

    def test_cart_url(self):
        """
        Test homepage response status
        """
        response = self.client.get(reverse('cart:cart_summary'))
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        """
        Test adding items to the cart
        """
        response = self.client.post(
            reverse('cart:cart_add'), {"product_id": 3, "product_qty": 1, "action": "POST"}, xhr=True)
        self.assertEqual(response.json(), {'product_quantity': 4})
        
        response = self.client.post(
            reverse('cart:cart_add'), {"product_id": 2, "product_qty": 1, "action": "POST"}, xhr=True)
        self.assertEqual(response.json(), {'product_quantity': 3})

    def test_cart_delete(self):
        """
        Test deleting items from the cart
        """
        response = self.client.post(
            reverse('cart:cart_delete'), {"product_id": 2, "action": "POST"}, xhr=True)
        self.assertEqual(response.json(), {'quantity': 1, 'subtotal': '31.50'}) # (Price * AMT) + 11.50 (tax)

    def test_cart_update(self):
        """
        Test updating items from the cart
        """
        response = self.client.post(
            reverse('cart:cart_update'), {"product_id": 2, "product_qty": 1, "action": "POST"}, xhr=True)
        self.assertEqual(response.json(), {'quantity': 2, 'subtotal': '51.50'})  # (Price * AMT) + 11.50 (tax)