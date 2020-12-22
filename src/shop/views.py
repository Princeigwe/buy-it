from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # viewing only available products
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product_shop/products.html', {'category': category, 
                                                        'categories': categories, 
                                                        'products': products
                                                        })

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'product_shop/product_details.html', {'product': product})
