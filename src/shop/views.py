from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CART_ADD_PRODUCT_FORM

# Create your views here.



def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    # viewing only available products
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'product_shop/index_product_list.html', {'category': category, 
                                                        'categories': categories, 
                                                        'products': products
                                                        })

# the product detail page calls the cart form when it's needed
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_add_product_form = CART_ADD_PRODUCT_FORM()
    return render(request, 'product_shop/product_details.html', {'product': product,
                                                                'cart_add_product_form': cart_add_product_form
                                                                })
