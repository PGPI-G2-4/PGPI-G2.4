from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Department,
    Medic,
    Event,
)

admin.site.register(Department)
admin.site.register(Medic)
admin.site.register(Event)
