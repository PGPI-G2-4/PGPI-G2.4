from django.contrib import admin

from .models import Appointment, OrderItem

admin.site.register(Appointment)
admin.site.register(OrderItem)