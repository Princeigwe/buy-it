from django.shortcuts import render,redirect, get_object_or_404
from .forms import OrderCreateForm
from .models import OrderItem, Order
from cart.cart import Cart
from .tasks import order_created
from django.conf import settings
from payments.views import paymentpage
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required
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
            # launching asynchronous task, delay method will add the task to queue and execute it once a worker is available
            #order_created.delay(order.id)
            #return render(request, 'orders/created_order.html', {'order': order})
            #return redirect('payments:payment')
            return redirect('payments:payment', id=order.id)
    
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create_order.html', {'cart': cart, 'form': form})

""" 
the order create view is used to place order after adding items to cart.
the view request for the cart, when the order create form is filled,
the order item model takes data of every item in the cart, and creates a model for it.
After that is done, the cart is cleared.
"""