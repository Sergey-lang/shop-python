from django.shortcuts import render


def home(request):
    context = {"categories": []}
    return render(request, 'shop/shop.html', context)
