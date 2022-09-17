
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        """
        Create test category object
        """
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_model_name(self):
        """
        Test Category model default name
        """
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        """
        Create a test product object 
        """
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(categories_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        # self.data2 = Product.products.create(category_id=1, title='django advanced', created_by_id=1,
        #                                      slug='django-advanced', price='20.00', image='django', is_active=False)

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')
