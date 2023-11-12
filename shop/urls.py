from django.urls import path

from shop.views import home, product_list_by_category, product_detail, get_cart, add_product_to_cart, \
    delete_product_from_cart, clean_all_cart, order_products

urlpatterns = [
    path('', home, name='home'),
    path('/category/<int:category_pk>', product_list_by_category, name='product_list_by_category'),
    path('/category/product/<int:product_pk>', product_detail, name='product_detail'),
    path('/cart/add_product/<int:product_pk>', add_product_to_cart, name='add_product_to_cart'),
    path('/cart/delete_product/<int:product_pk>', delete_product_from_cart, name='delete_product_from_cart'),
    path('/cart/clean_products', clean_all_cart, name='clean_all_cart'),
    path('/cart/order_products', order_products, name='order_products'),
    path('/cart', get_cart, name='get_cart'),
]
