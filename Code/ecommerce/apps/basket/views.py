from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from ecommerce.apps.catalogue.models import Department, Medic

from .basket import Basket
from ..orders.models import Appointment


def basket_summary(request):
    basket = Basket(request)
    return render(request, "basket/summary.html", {"basket": basket, "email": request.session["email"]})


def basket_add(request):
    # TODO: No permitir agregar citas a un mismo medic en el mismo horario
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("product_id"))
        meeting_time = datetime.strptime(request.POST.get("meeting_time"), "%Y-%m-%dT%H:%M")
        product = get_object_or_404(Medic, id=product_id)
        basket.add(medic=product, meeting_time=meeting_time)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})
        return response

def basket_add2(request, product_id, meeting_time):
    # TODO: No permitir agregar citas a un mismo medic en el mismo horario
        basket = Basket(request)    
        product = get_object_or_404(Medic, id=product_id)
        basket.add(medic=product, meeting_time=meeting_time)

        basketqty = basket.__len__()
        response = JsonResponse({"qty": basketqty})
        return response
        

def basket_delete(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        product_id = int(request.POST.get("appointment_id"))
        basket.delete(product=product_id)
        # Delete appointment from database
        Appointment.objects.get(id=product_id).delete()

        basketqty = basket.__len__()
        baskettotal = basket.get_total_price()
        response = JsonResponse({"qty": basketqty, "subtotal": baskettotal})
        return response


def basket_update(request):
    basket = Basket(request)
    if request.POST.get("action") == "post":
        appointment_id = request.POST.get("appointment_id")
        meeting_time = request.POST.get("meeting_time")
        basket.update(meeting_time=meeting_time, appointment_id=appointment_id)

        basketqty = basket.__len__()
        basketsubtotal = basket.get_subtotal_price()
        response = JsonResponse({"qty": basketqty, "subtotal": basketsubtotal})
        return response

