
from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey



class Department(models.Model):
    name = models.CharField(max_length=255, primary_key=True)

    def __str__(self):
        return self.name


class Medic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images/", blank=True, null=True, default="images/default.jpg")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="medics")
    regular_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    # Auto-generated slug field
    slug = models.SlugField(max_length=255, blank=True, null=True)

    # Def to generate slug
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Medic, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("catalogue:product_detail", args=[self.slug])

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    @property
    def get_html_url(self):
        url = reverse('calendar:event_edit', args=(self.id,))
        return f'<a href="{url}"> {self.title} </a>'
