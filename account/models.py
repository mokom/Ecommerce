import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, email, name, password, **extra_fields):

        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must be assigned to is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True.")

        return self.create_user(email, name, password, **extra_fields)

    def create_user(self, email, name, password, **extra_fields):

        if not email:
            raise ValueError(_("You must provide an email address"))

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, **extra_fields)
        user.set_password(password)
        user.save()
        return


class Customer(AbstractBaseUser, PermissionsMixin):  # Custom user class
    email = models.EmailField(verbose_name=_("Email"), max_length=254, unique=True)
    name = models.CharField(verbose_name=_("Name"), max_length=150)
    mobile_phone = models.CharField(verbose_name=_("Mobile Phone"), max_length=150, blank=True)
    # User status
    is_active = models.BooleanField(verbose_name=_("is_active"), default=False)
    is_staff = models.BooleanField(verbose_name=_("is_staff"), default=False)
    created = models.DateTimeField(verbose_name=_("Created"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Updated"), auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        verbose_name = _("Accounts")
        verbose_name_plural = _("Accounts")

    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            "l@1.com",
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.name


class Address(models.Model):
    """
    Address
    """

    id = models.UUIDField(_("ID"), primary_key=True, default=uuid.uuid4, editable=False)
    customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
    full_name = models.CharField(_("Full Name"), max_length=150)
    phone = models.CharField(_("Phone Number"), max_length=30)
    postal_code = models.CharField(_("Postal Code"), max_length=6)
    address_line1 = models.CharField(_("Address line 1"), max_length=255)
    address_line2 = models.CharField(_("Address line 2"), max_length=255)
    town_city = models.CharField(_("Town/City/State"), max_length=150)
    delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=250)
    created = models.DateTimeField(verbose_name=_("Created at"), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_("Updated at"), auto_now=True)
    default = models.BooleanField(_("Default"), default=False)

    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")

    def __str__(self):
        return self.customer.name
