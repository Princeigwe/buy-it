from django.shortcuts import render, get_object_or_404
from django.views.generic.base import  TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required


from orders.models import Order

# Create your views here.

@login_required
class PaymentPageView(TemplateView):
    template_name = 'paymentpage.html'
    
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.RAVE_PUBLIC_KEY
        order = get_object_or_404(Order, id=1)
        context['totalPrice'] = order.get_total_cost
        context['emailAddress'] = order.email
        return context


@login_required
def paymentpage(request, id):
    key = settings.RAVE_PUBLIC_KEY
    order = get_object_or_404(Order, id=id)
    totalPrice = order.get_total_cost()
    emailAddress = order.email
    telephone = order.telephone
    return render(request, 'paymentpage.html', {'key': key, 'totalPrice': totalPrice, 'emailAddress': emailAddress, 'telephone': telephone})


@login_required
def paymentsuccess(request):
    return render(request, "paymentsuccess.html")


@login_required
def paymentfailure(request):
    return render(request, 'paymentfailure.html')