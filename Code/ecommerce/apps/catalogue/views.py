import calendar
import queue
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render

from .models import Department, Medic
from ecommerce.apps.catalogue.forms import EventForm

from .utils import Calendar
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.db.models import Q
from datetime import date, datetime, timedelta

def product_all(request):
    busqueda = request.GET.get("buscar")
    products = Medic.objects.all()
   
    if busqueda:
        medico = Medic.objects.filter(
            Q(name__icontains = busqueda) | 
            Q(surname__icontains = busqueda)
        ).distinct()
        print(medico)
        return render(request, 'catalogue/medics.html', {'products':medico})
    return render(request, "catalogue/index.html", {"products": products})
   


def category_list(request, category_name=None):
    category = get_object_or_404(Department, name=category_name)
    products = Medic.objects.filter(department__name=category_name)
    return render(request, "catalogue/category.html", {"category": category, "products": products})




def product_detail(request, slug):
    product = get_object_or_404(Medic, slug=slug)
    return render(request, "catalogue/single.html", {"product": product})


class CalendarView(generic.ListView):
    model = Event
    template_name = 'catalogue/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        d = get_date(self.request.GET.get('day', None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('catalogue:calendar'))
    return render(request, 'catalogue/event.html', {'form': form})