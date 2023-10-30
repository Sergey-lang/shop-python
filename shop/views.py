from django.shortcuts import render
from django.shortcuts import get_object_or_404

from shop.models import Category, Product


def get_all_categories():
    return Category.objects.all()


def get_products_list(key=None):
    if key:
        return Product.objects.filter(category=key)
    return Product.objects.all()


def get_product_detail(key):
    return get_object_or_404(Product, pk=key)


def home(request):
    categories = get_all_categories()
    products = get_products_list()
    context = {"categories": categories, 'products': products}
    return render(request, 'shop/home.html', context)


def product_list_by_category(request, category_pk):
    products_by_category = get_products_list(category_pk)
    categories = get_all_categories()
    context = {"categories": categories, 'products': products_by_category}
    return render(request, 'shop/home.html', context)


def product_detail(request, product_pk):
    product = get_product_detail(product_pk)
    categories = get_all_categories()
    context = {"categories": categories, 'product': product}
    return render(request, 'shop/product_detail.html', context)
