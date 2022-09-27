from django.conf import settings
from django.db import models
from django.utils.translation import gettext as _

from store.models import Product


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("User"), on_delete=models.CASCADE, related_name='order_user')
    full_name = models.CharField(_("Full Name"), max_length=50)
    address1 = models.CharField(_("Address1"), max_length=250)
    address2 = models.CharField(_("Address2"), max_length=250)
    city = models.CharField(_("City"), max_length=100)
    phone = models.CharField(_("Phone"), max_length=100)
    postal_code = models.CharField(_("Postal_Code"), max_length=20)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)
    total_paid = models.DecimalField(_("Total_Paid"), max_digits=5, decimal_places=2)
    order_key = models.CharField(_("Order key"), max_length=200)
    billing_status = models.BooleanField(_("Billing Status"), default=False)

    class Meta:
        ordering = ('-created',)
    
    def __str__(self):
        return str(self.created)


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
