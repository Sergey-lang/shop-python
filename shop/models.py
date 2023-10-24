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
