from django.shortcuts import render

from .models import Product



def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', context={'products': products})


def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'products/product-detail.html', context={'product': product})