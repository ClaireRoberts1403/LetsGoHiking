from django.db import models


CATEGORY = (
    ("Patches", "Patches"),
    ("Stickers", "Stickers"),
    ("Hats", "Hats"),
    ("WaterBottle", "WaterBottle"),
)


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=254)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.TextField()
    category = models.ForeignKey('category', null=True, blank=True, on_delete=models.SET_NULL)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
