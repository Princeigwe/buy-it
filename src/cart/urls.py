from django.urls import path
from .import views

app_name='cart'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<int:product>/', views.cart_add_product, name='add_product'),
    path('remove/<int:product>/', views.cart_remove_product, name='remove_product')
]
