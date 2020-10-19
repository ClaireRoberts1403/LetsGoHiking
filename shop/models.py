from django.db import models


class category(models.Model):

    class Meta:
        verbose_name_plural = 'categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


CATEGORY = (
    ("Patches"),
    ("Stickers"),
    ("Hats"),
    ("Water Bottle"),
)


class product(models.Model):
    name = models.CharField(max_length=254)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.TextField()
    category = models.ForeignKey('category', max_length=20, choices=CATEGORY, on_delete=models.SET_NULL)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
