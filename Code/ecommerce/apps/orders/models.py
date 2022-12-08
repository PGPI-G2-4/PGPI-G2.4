from decimal import Decimal

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from ecommerce.apps.catalogue.models import Medic

class Appointment(models.Model):
    id = models.AutoField(primary_key=True)
    date_time = models.DateTimeField(_("Date and time of appointment"))
    client_name = models.CharField(max_length=255)
    client_surname = models.CharField(max_length=255)
    client_email = models.EmailField(_("email address"))
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE, related_name="appointments")

    unique_together = ("date_time", "medic")
    unique_together = ("medic.department", "client_email")


    def clean(self):
        # Date must be 3 days in the future
        if self.date_time < timezone.now() + timezone.timedelta(days=3):
            raise ValidationError(_("La cita debe realizarse con al menos 3 días de antelación"))

        # There must not be another appointment in the next 30 minutes for the same medic
        if Appointment.objects.filter(
            medic=self.medic, date_time__range=(self.date_time, self.date_time + timezone.timedelta(minutes=30))
        ).exists():
            raise ValidationError(_("Ya existe una cita para ese médico en ese horario"))

        # Appointments must be in working hours
        if self.date_time.hour < 8 or self.date_time.hour > 20:
            raise ValidationError(_("Las citas deben ser entre las 8 y las 20 horas"))

    def __str__(self):
        return f"{self.medic} - {self.date_time} | {self.client_name} {self.client_surname}"


    class Meta:
        ordering = ["date_time"]


class OrderItem(models.Model):
    appointment = models.ForeignKey(Appointment, related_name="items", on_delete=models.CASCADE)
    medic = models.ForeignKey(Medic, related_name="order_items", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
