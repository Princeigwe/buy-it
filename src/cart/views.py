from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CART_ADD_PRODUCT_FORM


# Create your views here.

# view for adding product to cart
@require_POST
def cart_add_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CART_ADD_PRODUCT_FORM(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            override_quantity=cd['override']
        )
    return redirect('cart:cart_detail')

#view for removing product from the cart
@require_POST
def cart_remove_product(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    # for each item in the cart...
    for item in cart:
        # initialize the cart form with product quantity and set override to true, so that quantity can be updated if the user wants to
        item['update_quantity_form'] = CART_ADD_PRODUCT_FORM(initial={'quantity': item['quantity'], 'override': True})
    return render(request, 'product_shop/cart.html', {'cart': cart})
