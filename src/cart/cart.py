from decimal import Decimal
from django.conf import settings
from shop.models import Product

class Cart(object):

    def __init__(self, request):
        #initializing the cart

        #accessing the session
        self.session = request.session
        # getting the cart key in user session
        cart = self.session.get(settings.CART_SESSION_ID)

        #if there's no current key in user session...
        if not cart:
            # create an empty cart key
            cart = self.session[settings.CART_SESSION_ID] = {}
            self.cart = cart

    #method for adding product
    def add(self, product, quantity=1, override_quantity=False):
        """
        adding or updating product
        """
        # assigning the product id
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}

        # if quantity is overidden...
        if override_quantity:
            # the value of the key quqntity of key product_id of the cart is 1
            self.cart[product_id] ['quantity'] = quantity
        else:
            self.cart[product_id] ['quantity'] += quantity
        self.save()

    # save function
    def save(self):
        # mark the session as "modified" to make sure it gets saved
        self.session.modified = True

    # the remove function for cart
    def remove(self, product):
        product_id = product.id
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    #method for iterating through items in cart and getting them from the database
    def __iter__(self):
        #all products in the cart
        product_ids = self.cart.keys
        # getting the product objects and adding to the cart
        products = Product.objects.filter(id__in=product_ids)

        # copy the cart
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        # for each product item in cart...
        for item in cart.values():
            #product item price is a decimal format
            item['price'] = Decimal(item['price'])
            # total price of product items in the cart
            item['total_price'] = item['price'] * item['quantity']
            yield item

    #method for counting all product items in the the cart
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())

    #method for getting total price of all products int the cart
    def get_total_price(self):
        return sum(item['price'] * item['quantity'] for item in self.cart.values())

    #method for clearing the cart
    def clear(self):
        del self.cart
        self.save()
