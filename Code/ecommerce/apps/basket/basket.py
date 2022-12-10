from datetime import datetime
from decimal import Decimal

from django.conf import settings
from django.shortcuts import get_object_or_404

from ecommerce.apps.catalogue.models import Medic
from ecommerce.apps.orders.models import Appointment
from ecommerce.apps.checkout.models import DeliveryOptions



class Basket:
    """
    A base Basket class, providing some default behaviors that
    can be inherited or overrided, as necessary.
    """

    def create_appointment(self, medic, meeting_time):
        appointment = Appointment.objects.create(
            medic=medic,
            price=medic.regular_price,
            date_time=meeting_time,
            client_email=self.session["email"],
        )
        return appointment

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get(settings.BASKET_SESSION_ID)
        if settings.BASKET_SESSION_ID not in request.session:
            basket = self.session[settings.BASKET_SESSION_ID] = {}
        self.basket = basket
        # add a temporal email to the session
        if "email" not in request.session:
            self.session["email"] = datetime.now().strftime("%Y%m%d%H%M%S") + "@temporal.com"

    def add(self, medic, meeting_time):
        """
        Adding and updating an appointment in the session data
        """
        print("Trying to create appointment")
        # Create appointment
        appointment = self.create_appointment(medic, meeting_time)
        # Save appointment in the session
        self.basket[appointment.id] = {"meeting_time": str(meeting_time), "price": str(medic.regular_price)}
        self.save()
        print("Appointment added to the basket")


        # product_id = str(product.id)
        #
        # if product_id in self.basket:
        #     self.basket[product_id]["meeting_time"] = meeting_time
        # else:
        #     self.basket[product_id] = {"price": str(product.regular_price), "meeting_time": meeting_time}
        #
        # self.save()

    def __iter__(self):
        """
        Collect the product_id in the session data to query the database
        and return products
        """
        product_ids = self.basket.keys()
        products = Appointment.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]["product"] = product

        for item in basket.values():
            if item["price"] != 'None':
                item["price"] = Decimal(item["price"])
            else:
                item["price"] = 0.00
            yield item

    def __len__(self):
        """
        Get the basket data and count the qty of items
        """
        return sum(1 for _ in self.basket.values())

    def update(self, meeting_time, appointment_id):
        """
        Update values in session data
        """
        if appointment_id in self.basket:
            self.basket[appointment_id]["meeting_time"] = str(meeting_time)
            # Save new date to the appointment
            appointment = Appointment.objects.get(id=appointment_id)
            appointment.date_time = meeting_time
            appointment.save()
            self.save()


    def get_subtotal_price(self):
        return sum(Decimal(item["price"]) for item in self.basket.values() if item["price"] != 'None')

    def get_delivery_price(self):
        newprice = 0.00

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        return newprice

    def get_total_price(self):
        newprice = 0.00
        subtotal = self.get_subtotal_price()

        if "purchase" in self.session:
            newprice = DeliveryOptions.objects.get(id=self.session["purchase"]["delivery_id"]).delivery_price

        total = subtotal + Decimal(newprice)
        return total

    def basket_update_delivery(self, deliveryprice=0):
        subtotal = sum(Decimal(item["price"]) for item in self.basket.values())
        total = subtotal + Decimal(deliveryprice)
        return total

    def delete(self, product):
        """
        Delete item from session data
        """
        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def clear(self):
        # Remove basket from session
        del self.session[settings.BASKET_SESSION_ID]
        del self.session["email"]
        del self.session["purchase"]
        self.save()

    def save(self):
        self.session.modified = True
