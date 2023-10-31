from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)

    def __str__(self):
        return f'{self.title}'


class Product(models.Model):
    title = models.CharField(verbose_name="Title", max_length=50)
    description = models.TextField(verbose_name="Description", max_length=250)
    price = models.DecimalField(verbose_name="price", decimal_places=2, max_digits=10)
    category = models.ForeignKey('Category', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}'


class Card(models.Model):
    number = models.CharField(verbose_name="Card number", max_length=16)
    month = models.CharField(verbose_name="Month", max_length=2)
    year = models.CharField(verbose_name="Year", max_length=2)
    cvc = models.CharField(verbose_name="CVC", max_length=16)
    card_name = models.CharField(verbose_name="Card name", max_length=64)

    def __str__(self):
        return f'{self.card_name}'


class Cart(models.Model):
    user = models.OneToOneField("auth.USER", on_delete=models.CASCADE)
    products = models.ManyToManyField("Product", related_name="Products")

    def __str__(self):
        return f'{self.user}'
