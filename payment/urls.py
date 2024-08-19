from django.urls import path
from . import views

urlpatterns = [
    path('payment_success', views.payment_success, name = "payment_success"),
    path('checkout', views.checkout, name = "checkout"),
    path('billing_info', views.billing_info, name="billing_info"),
    path('process_order', views.process_order, name="process_order"),
    path('order_history/', views.order_history, name='order_history'),
    path('order/<int:pk>', views.orders, name='orders'),
]