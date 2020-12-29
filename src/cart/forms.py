from django import forms

PRODUCT_QUANTITY_CHOICE = [ (i, str(i)) for i in range(1,21) ]

class CART_ADD_PRODUCT_FORM(forms.Form):
    # creating a dropdown list of quantity of products to be bought
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICE, coerce=int)
    # for changing the quantity of product if it is different from the initial value
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)