
import uuid

from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin, AbstractUser,
)
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.core.validators import validate_email
from django.db import models
from django.utils.translation import gettext_lazy as _

from ecommerce.apps.catalogue.models import Event

tipo_incidencia=[
    (1,'Anular cita'),
    (2, 'Cambio de mi perfil'),
    (3, 'Otros')
]

class Customer(AbstractUser):
    class Gender(models.TextChoices):
        MALE = "M", "Male"
        FEMALE = "F", "Female"

    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=30, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    age = models.PositiveIntegerField(_("Age"), null=True, blank=True)
    gender = models.CharField(max_length=1, choices=Gender.choices)
    region = models.CharField(max_length=150)
    alergies = models.CharField(max_length=150)
    pathologies = models.CharField(max_length=150)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


    class Meta:
        verbose_name = "Accounts"
        verbose_name_plural = "Accounts"

    def __str__(self):
        return self.first_name + " " + self.last_name



class Incidencia(models.Model):
    
    id = models.AutoField(primary_key=True)
    client_email = models.EmailField(_("email address"))
    Tipo= models.IntegerField(
        null=False , blank=False,
        choices= tipo_incidencia
    )
    Descripcion = models.CharField(max_length=1000)
    evento = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="evento",null=True)
    
    
    



