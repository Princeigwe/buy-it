from celery import task
from django.core.mail import send_mail
from .models import Order

from django.shortcuts import render, get_object_or_404
#from django.views.generic.base import  TemplateView
from django.conf import settings
from django.contrib.auth.decorators import login_required


@task
def order_created(order_id):
    "task to send an email notification when an order is created"
    order = Order.objects.get(id=order_id)
    subject = f'Order nr .{order.id}'
    message =   f'Dear {order.first_name}, \n\n '\
                f'You have successfully placed an order. \n'\
                f'Your order id is {order.id} .'
    mail_sent = send_mail(subject, message, 'admin@buy_it.com', {order.email})
    return mail_sent


@task
def paymentpage_task(request, id):
    key = settings.RAVE_PUBLIC_KEY
    order = get_object_or_404(Order, id=id)
    totalPrice = order.get_total_cost()
    emailAddress = order.email
    telephone = order.telephone
    return render(request, 'paymentpage.html', {'key': key, 'totalPrice': totalPrice, 'emailAddress': emailAddress, 'telephone': telephone})

@task
@login_required
def paymentsuccess(request):
    return render(request, "paymentsuccess.html")

@task
@login_required
def paymentfailure(request):
    return render(request, 'paymentfailure.html')