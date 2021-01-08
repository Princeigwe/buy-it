from django.shortcuts import render
from .forms import OrderCreateForm
from .models import OrderItem
from cart.cart import Cart


# Create your views here.

def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            # for each item in cart...
            for item in cart:
                # create an order item for it
                OrderItem.objects.create(order=order, product=item['product'], price=(item['price']), quantity=item['quantity'] )
            
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'cart': cart, 'form': form})

""" 
the order create view is used to place order after adding items to cart.
the view request for the cart, when the order create form is filled,
the order item model takes data of every item in the cart, and creates a model for it.
After that is done, the cart is cleared.
"""