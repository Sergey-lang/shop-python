from django.urls import path

from shop.views import home, product_list_by_category, product_detail
urlpatterns = [
    path('', home, name='home'),
    path('/category/<int:category_pk>', product_list_by_category, name='product_list_by_category'),
    path('/category/product/<int:product_pk>', product_detail, name='product_detail'),
]
