from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Category Table implemented with MPTT
    """

    name = models.CharField(verbose_name=_("name"), help_text=_("Required and unique"), max_length=255, unique=True)
    slug = models.SlugField(verbose_name=_("Category safe URL"), max_length=255)
    parent = TreeForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(verbose_name=_("Is_active"), default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    """
    ProductType Table will provide a list of the different types of products that are for sale
    """

    name = models.CharField(verbose_name=_("Product Name"), help_text=_("Required"), max_length=255)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    """
    The Product Specification Table contains product specification or features for the product types
    """

    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    name = models.CharField(verbose_name=_("Name"), help_text=_("Required"), max_length=255)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    """
    The product table containing all product items
    """

    product_type = models.ForeignKey(ProductType, verbose_name=_("Product Type"), on_delete=models.RESTRICT)
    category = models.ForeignKey(Category, verbose_name=_("Category"), on_delete=models.RESTRICT)
    title = models.CharField(verbose_name=_("Title"), help_text=_("Required"), max_length=255)
    description = models.TextField(_("Description"), help_text=_("description"), blank=True)
    slug = models.SlugField(_("Slug"), max_length=255, unique=True)
    regular_price = models.DecimalField(
        _("Price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    discount_price = models.DecimalField(
        _("Discount Price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(_("Product visibility"), help_text=_("Change product visibility"), default=True)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)
    users_wishlist = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True)

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ("-created_at",)

    def get_absolute_url(self):
        return reverse("store:product_detail", args=[self.slug])

    def __str__(self):
        return self.title


class ProductSpecificationValue(models.Model):
    """
    The product specification value table holds each of the products individual
    specification or bespoke features
    """

    product = models.ForeignKey(Product, verbose_name=_("Product"), on_delete=models.CASCADE)
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("value"), help_text=_("Product specification value (maximum of 255 words)"), max_length=255
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    """
    The product Image table
    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_image")
    image = models.ImageField(
        verbose_name=_("Alternative text"),
        help_text=_("Please add alternative text"),
        max_length=255,
        null=True,
        blank=True,
    )
    is_feature = models.BooleanField(verbose_name=_("Is this a feature Image?"), default=False)
    created_at = models.DateTimeField(_("Created"), auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(_("Updated"), auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
