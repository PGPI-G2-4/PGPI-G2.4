import json

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from ecommerce.apps.basket.basket import Basket
from ecommerce.apps.orders.models import Appointment, OrderItem

from .models import DeliveryOptions
from ..catalogue.models import Event
from ... import settings


def deliverychoices(request):
    deliveryoptions = DeliveryOptions.objects.filter(is_active=True)
    return render(request, "checkout/delivery_choices.html", {"deliveryoptions": deliveryoptions, "email": request.session["email"]})



def basket_update_delivery(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        delivery_option = int(request.POST.get("deliveryoption"))
        delivery_type = DeliveryOptions.objects.get(id=delivery_option)
        updated_total_price = basket.basket_update_delivery(delivery_type.delivery_price)

        session = request.session
        if "purchase" not in request.session:
            session["purchase"] = {
                "delivery_id": delivery_type.id,
            }
        else:
            session["purchase"]["delivery_id"] = delivery_type.id
            session.modified = True

        response = JsonResponse({"total": updated_total_price, "delivery_price": delivery_type.delivery_price, "sub_total": basket.get_subtotal_price()})
        return response



def delivery_address(request):

    email = request.session["email"]
    basket = Basket(request)
    if "purchase" not in request.session:
        messages.success(request, "Please select delivery option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])


    return render(request, "checkout/delivery_address.html", {"email": email, "basket": basket})



def payment_selection(request):

    session = request.session
    basket = Basket(request)
    if "temporal" in request.session["email"]:
        messages.success(request, "Please select address option")
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    return render(request, "checkout/payment_selection.html", {'basket': basket, "email": request.session["email"]})



def payment_successful(request):
    basket = Basket(request)
    send_confirmation_email(request.session["email"])
    basket.clear()
    return render(request, "checkout/payment_successful.html", {})

def send_confirmation_email(email):
    subject = "Gracias por confiar en CIT@MEDICA!"
    message = "Se ha realizado tu pedido. Si quieres revisar tus citas puedes hacerlo ingresando tu correo electrónico en la página de inicio."
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, auth_password=settings.EMAIL_HOST_PASSWORD)


# Updates the session's email address to the new one
def update_email(request):
    if request.method == "POST":
        new_email = request.POST.get("email")
        old_email = request.session["email"]
        request.session["email"] = new_email
        # Update the email address in the database
        Appointment.objects.filter(client_email=old_email).update(client_email=new_email)
        Event.objects.filter(client_email=old_email).update(client_email=new_email)

        return HttpResponse("Success")
    else:
        return HttpResponse("Error")
