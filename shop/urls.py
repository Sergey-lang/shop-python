from django.urls import path

from shop.views import home, product_list_by_category, product_detail, get_cart, add_product_to_cart
urlpatterns = [
    path('', home, name='home'),
    path('/category/<int:category_pk>', product_list_by_category, name='product_list_by_category'),
    path('/category/product/<int:product_pk>', product_detail, name='product_detail'),
    path('/cart/add_product/<int:product_pk>', add_product_to_cart, name='add_product_to_cart'),
    path('/cart', get_cart, name='get_cart'),
]
