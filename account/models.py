from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core.mail import send_mail
from django.db import models
from django.utils.translation import gettext as _
from django_countries.fields import CountryField


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, user_name, password, **extra_fields):
        
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(email, user_name, password, **extra_fields)

    def create_user(self, email, user_name, password, **extra_fields):

        if not email:
            raise ValueError(_('You must provide an email address'))

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=user_name, **extra_fields)
        user.set_password(password)
        user.save()
        return 

class UserBase(AbstractBaseUser, PermissionsMixin): # Custom user class
    email = models.EmailField(_("Email"), max_length=254, unique=True)
    user_name = models.CharField(_("Username"), max_length=150, unique=True)
    first_name = models.CharField(_("First_Name"), max_length=150, blank=True)
    about = models.TextField(_("About"), max_length=500, blank=True)
    # Delivery Details
    country = CountryField()
    phone_number = models.CharField(_("Phone_Number"), max_length=15, blank=True)
    postal_code = models.CharField(_("Poastal_code"), max_length=12, blank=True)
    address_line_1 = models.CharField(_("Address_line_1"), max_length=150, blank=True)
    address_line_2 = models.CharField(_("Address_line_2"), max_length=150, blank=True)
    # User status
    is_active = models.BooleanField(_("is_active"), default=False)
    is_staff = models.BooleanField(_("is_staff"), default=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    objects = CustomAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["user_name"]

    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"


    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'l@1.com',
            [self.email],
            fail_silently=False,
        )

    def __str__(self):
        return self.user_name
    


