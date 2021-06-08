from django.urls import path
from . import views

app_name = 'payments'

urlpatterns = [
    #path('payment/', views.PaymentPageView.as_view(), name='payment'),
    path('payment/<int:id>/', views.paymentpage, name='payment'),
    path('paymentsuccess.html', views.paymentsuccess, name='success'),
    path('paymentfailure.html', views.paymentfailure, name='failure'),
]