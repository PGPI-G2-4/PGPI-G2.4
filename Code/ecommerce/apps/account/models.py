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


# class CustomAccountManager(BaseUserManager):
#     # def validateEmail(self, email):
#     #     try:
#     #         validate_email(email)
#     #     except ValidationError:
#     #         raise ValueError(_("You must provide a valid email address"))
#
#     def create_superuser(self, email, name, password, **other_fields):
#
#         other_fields.setdefault("is_staff", True)
#         other_fields.setdefault("is_superuser", True)
#         other_fields.setdefault("is_active", True)
#
#         if other_fields.get("is_staff") is not True:
#             raise ValueError("Superuser must be assigned to is_staff=True")
#         if other_fields.get("is_superuser") is not True:
#             raise ValueError("Superuser must be assigned to is_superuser=True")
#
#         if email:
#             email = self.normalize_email(email)
#             self.validateEmail(email)
#         else:
#             raise ValueError(_("Superuser Account: You must provide an email address"))
#
#         return self.create_user(email, name, password, **other_fields)
#
#     def create_user(self, email, name, password, **other_fields):
#
#         if email:
#             email = self.normalize_email(email)
#             self.validateEmail(email)
#         else:
#             raise ValueError(_("Customer Account: You must provide an email address"))
#
#         email = self.normalize_email(email)
#         user = self.model(email=email, name=name, **other_fields)
#         user.set_password(password)
#         user.save()
#         return user


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


# class Address(models.Model):
#     """
#     Address
#     """
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     customer = models.ForeignKey(Customer, verbose_name=_("Customer"), on_delete=models.CASCADE)
#     full_name = models.CharField(_("Full Name"), max_length=150)
#     phone = models.CharField(_("Phone Number"), max_length=50)
#     postcode = models.CharField(_("Postcode"), max_length=50)
#     address_line = models.CharField(_("Address Line 1"), max_length=255)
#     address_line2 = models.CharField(_("Address Line 2"), max_length=255)
#     town_city = models.CharField(_("Town/City/State"), max_length=150)
#     delivery_instructions = models.CharField(_("Delivery Instructions"), max_length=255)
#     created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
#     updated_at = models.DateTimeField(_("Updated at"), auto_now=True)
#     default = models.BooleanField(_("Default"), default=False)
#
#     class Meta:
#         verbose_name = "Address"
#         verbose_name_plural = "Addresses"
#
#     def __str__(self):
#         return "{} Address".format(self.full_name)
