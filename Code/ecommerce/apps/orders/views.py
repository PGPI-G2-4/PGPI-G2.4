from django.http.response import JsonResponse
from django.shortcuts import render
from ecommerce.apps.basket.basket import Basket

from .models import Appointment, OrderItem


def add(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":

        order_key = request.POST.get("order_key")
        user_id = request.user.id
        baskettotal = basket.get_total_price()

        # Check if order exists
        if Appointment.objects.filter(order_key=order_key).exists():
            pass
        else:
            order = Appointment.objects.create(
                user_id=user_id,
                full_name="name",
                total_paid=baskettotal,
                order_key=order_key,
            )
            order_id = order.pk

            for item in basket:
                OrderItem.objects.create(
                    order_id=order_id, product=item["product"], price=item["price"], quantity=item["qty"]
                )

        response = JsonResponse({"success": "Return something"})
        return response


def payment_confirmation(data):
    Appointment.objects.filter(order_key=data).update(billing_status=True)


def user_orders(request):
    user_id = request.user.id
    orders = Appointment.objects.filter(user_id=user_id).filter(billing_status=True)
    return orders
