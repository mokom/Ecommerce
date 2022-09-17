from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.translation import gettext as _

class Category(models.Model):
    name = models.CharField(_("name"), max_length=255, db_index=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])
    

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("Category"), related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, verbose_name=_("Created by"), on_delete=models.CASCADE, related_name="product_creator")
    title = models.CharField(_("Title"), max_length=255)
    author = models.CharField(_("Author"), max_length=255, default='admin')
    description = models.TextField(_("Description"), blank=True)
    image = models.ImageField(_("Image"), upload_to="images/")
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    price = models.DecimalField(_("Price"), max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(_("In Stock"), default=True)
    is_active = models.BooleanField(_("Is_Active"), default=True)
    created = models.DateTimeField(_("Created"), auto_now_add=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        verbose_name_plural = "Products"
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title
        
    
