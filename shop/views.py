from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from shop.models import Category, Product, Cart, Card


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


def add_product_to_cart(request, product_pk):
    product = get_product_detail(product_pk)
    product_to_card = Cart.objects.create(user=request.user)
    product_to_card.products.add(product)
    return redirect('shop/product_detail.html', product_pk=product_pk)


def get_cart(request):
    cart_by_user = Cart.objects.get(user=request.user)
    cart_products = cart_by_user.products
    categories = get_all_categories()
    context = {"categories": categories, 'cart_products': cart_products}
    return render(request, 'shop/product_detail.html', context)
