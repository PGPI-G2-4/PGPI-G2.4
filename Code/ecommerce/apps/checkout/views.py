import json
from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import render
from ecommerce.apps.account.models import Customer
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

    if request.session["purchase"]["delivery_id"] == 1:
        return render(request, "checkout/delivery_address.html", {"email": email, "basket": basket})
    elif request.session["purchase"]["delivery_id"] == 2:
        return render(request, "checkout/delivery_address_options.html", {"email": email, "basket": basket})

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
    send_confirmation_email(request.session["email"], basket)
    basket.clear()
    return render(request, "checkout/payment_successful.html", {})

def send_confirmation_email(email, basket):
    subject = "Gracias por confiar en CIT@MEDICA!"
    message = "Se ha realizado tu pedido. Si quieres revisar tus citas puedes hacerlo ingresando tu correo electrónico en la página de inicio."
    message = message + "\n # Datos del pedido #"
    message = message + "\n Fecha de pedido: " + str(datetime.now())
    message = message + "\n Email: " + email
    message = message + "\n # Productos #"
    for item in basket:
        message = message + "\n - " + item["product"].medic.name +" " +item["product"].medic.surname + " " + "Fecha: " + str(item["product"].date_time) +" " + "Precio: " + str(item["product"].medic.regular_price)
    message = message + "\n # Total #"
    message = message + "\n" + str(basket.get_total_price())

    message = message + "\n Esperamos que tenga una buena experiencia con nosotros."
    message = message + "\n Saludos, CIT@MEDICA"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list, auth_password=settings.EMAIL_HOST_PASSWORD)

def rellenar(request):
    email_session = request.session["email"]
    basket = Basket(request)
      
    a = Customer.objects.filter(email=email_session)
    num_items = len(a)

    if num_items>0:
        return render(request, "checkout/delivery_address_rellenar.html", {'opcion': False,"email": email_session, "basket": basket})

    elif num_items==0:
        return render(request, "checkout/delivery_address_rellenar.html", {'opcion': True,"email": email_session, "basket": basket})        
        
        
        
       
    


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

def update_email2(request):
    if request.method == "POST":
    
        old_email = request.session["email"]
        first_name1 = request.POST.get("first_name")
        last_name1= request.POST.get("last_name")
        age1 = request.POST.get("age")
        gender1 = request.POST.get("gender")
        alergies1 = request.POST.get("alergies")
        pathologies1= request.POST.get("pathologies")
        
        user = Customer()
        user.first_name = first_name1
        user.last_name = last_name1
        user.gender = gender1
        user.alergies = alergies1
        user.pathologies = pathologies1
        user.age = age1
        user.username = old_email
        user.email = old_email
        user.save()
        
        
        return HttpResponse("Success")   
    else:
        return HttpResponse("Error")



